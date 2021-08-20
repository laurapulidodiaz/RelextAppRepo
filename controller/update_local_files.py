import urllib 
from bs4 import BeautifulSoup
import pandas as pd
from zipfile import ZipFile
from io import BytesIO
import urllib.request
from pathlib import Path
import os
from datetime import datetime
import time
                          
URL_IMPORTS = "http://microdatos.dane.gov.co/index.php/catalog/473/get_microdata"
URL_EXPORTS = "http://microdatos.dane.gov.co/index.php/catalog/472/get_microdata"

URL_METADATA_IMPORTACIONES = "http://microdatos.dane.gov.co/index.php/catalog/473/datafile/F10"
URL_METADATA_EXPORTACIONES = "http://microdatos.dane.gov.co/index.php/catalog/472/datafile/F3"

PATH = "Data/CSV/"

INIT_YEAR = 2011
FINAL_YEAR = datetime.today().year
EXT = ".csv"

def url_list_from_web_e(URL) :
    file_name = []
    file_url = []

    r = urllib.request.urlopen(URL)
    site_content = r.read().decode('utf-8')

    with open('saved_temp.html', 'w') as f:
        f.write(site_content)

    soup = BeautifulSoup(site_content, 'html.parser')

    for span_block in soup.findAll('span', href=False, attrs={'class':'resource-file-size'}):
        input_block = span_block.find('input', attrs={'src':'images/page_white_compressed.png'})
        try:
            value = input_block['onclick'].split(",")        
            file_name.append(value[0][14:-2])
            file_url.append(value[1][2:-3]) 
        except:pass

    df = pd.DataFrame({'file_name':file_name,'file_url':file_url}) 
    f.close()
    os.remove("saved_temp.html")
    return df

def get_year_from_name(file_name) :
    return file_name[-8:-4]

def get_list_of_files() :
    global URL_EXPORTS
    global URL_IMPORTS
    
    df_exports = url_list_from_web_e(URL_EXPORTS)
    df_exports['type'] = "Exportaciones"
    df_exports['year'] = df_exports.apply(lambda x: get_year_from_name(x['file_name']),axis=1)

    df_imports = url_list_from_web_e(URL_IMPORTS)
    df_imports['type'] = "Importaciones"
    df_imports['year'] = df_imports.apply(lambda x: get_year_from_name(x['file_name']),axis=1)

    df = df_imports.append(df_exports, sort=False)
    df = df[['type', 'year', 'file_url']]
    df = df.reset_index().drop(columns=['index'])
    return df

def check_file_exist(type_s,year,month) :
    global PATH
    global EXT
    return os.path.isfile(PATH+type_s+"/"+str(year)+"/"+month+EXT)

def save_file_data(file, path_file, filename) :
    global PATH
    try:
        Path(PATH+path_file).mkdir(parents=True, exist_ok=True)
        complete_path = PATH + path_file + "/"+ filename
        f = open(complete_path, "wb")
        f.write(file.read())
        f.close()
        print("Archivo cargado.")
    except Exception as e:
        print("Ya existe.")
        print(e)
        
def check_full_year(type_s, year) :
    global PATH
    DIR = PATH+type_s+"/"+str(year)
    try :
        count_of_files = len(os.listdir(DIR))
        return count_of_files >= 12 
    except : 
        return False

def download_new_data_from_dane(df) :
    global INIT_YEAR
    global FINAL_YEAR
    for type_s in ("Exportaciones","Importaciones") :
        for year_s in range(INIT_YEAR, FINAL_YEAR+1) :
            if check_full_year(type_s, year_s) :
                continue

            dict_months ={
                "Enero": False,
                "Febrero":False,
                "Marzo":False,
                "Abril":False,
                "Mayo":False,
                "Junio":False,
                "Julio":False,
                "Agosto":False,
                "Septiembre":False,
                "Octubre":False,
                "Noviembre":False,
                "Diciembre":False }

            adjust_names = []
            try:
                url_current_year = df['file_url'][(df['type']==str(type_s)) & (df['year']==str(year_s))].values[0]
                print("Descarga: ",url_current_year,str(type_s),str(year_s))
            except:
                print("No hay URL de descarga para este archivo: ",str(type_s),str(year_s))
                continue

            # descargo el archivo de la URL, lo descomprimo y lo guardo
            r = urllib.request.urlopen(url_current_year).read()

            year_filebytes = BytesIO(r)
            year_zipfile = ZipFile(year_filebytes)

            path_data = type_s + "/" + str(year_s)

            for name in year_zipfile.namelist():
                if name.endswith('.zip') :
                    head, tail = os.path.split(name)
                    zip_to_open = tail 
                    head, sep, tail = tail.partition(' ')
                    if head.endswith('.zip') :
                        name_for_file = head[0:-5]
                    else :
                        name_for_file = head

                    month=year_zipfile.open(name)
                    try :
                        month_zipfile = ZipFile(month)
                        for name_f in month_zipfile.namelist():
                            if name_f.endswith(EXT) :
                                month_csv = month_zipfile.open(name_f)
                                name = name_f.replace(str(year_s),"")
                                name = name.replace(EXT,"")
                                name = name.replace("_","")
                                name = name.replace(" ","")
                                name = name.strip()

                                if name in list(dict_months.keys()) :
                                    dict_months[name] = True
                                else :
                                    adjust_names.append(name)

                                print(name+EXT)
                                if check_file_exist(type_s,year_s,name) != True :
                                    print("Tipo: "+type_s+", Año: "+str(year_s), "Archivo: "+name+EXT)
                                    save_file_data(month_csv, path_data, name+EXT)
                    except BadZipFile : 
                        pass
            if len(adjust_names) > 0 :
                pending = ""
                for key, value in dict_months.items() :
                    if not value :
                        pending = key
                        break
                if pending != "" :
                    try :
                        old_file = PATH + path_data + "/" + adjust_names[0] + EXT
                        new_file = PATH + path_data + "/" + pending + EXT
                        print("Renombrando:",old_file, "->", new_file)
                        os.rename(old_file, new_file)
                    except :
                        continue
                        
def url_list_from_web(URL) :
    column_name = []
    column_description = []
    column_details = []
    column_details_name = []
    column_details_values = []

    r = urllib.request.urlopen(URL)
    site_content = r.read().decode('utf-8')

    with open('saved_temp.html', 'w') as f:
        f.write(site_content)

    soup = BeautifulSoup(site_content, 'html.parser')

    for tr_block in soup.findAll('tr', href=False, attrs={'title':'Haga clic aquí para ver información de la variable'}):
        td_block = tr_block.findAll('td')
        try:     
            for br in td_block[2].find_all("br"):
                br.replace_with("-o-")
            
            value_string = td_block[2].text
            value_string_tolist = value_string.split("-o-")
            counter = 0
            for value_str in value_string_tolist :
                value_str = value_str.strip(' \t\n\r')
                value_str = value_str.replace('\t',' ')
                if value_str != "" :
                    if counter == 0 :
                        column_name.append(td_block[0].text)
                        column_description.append(td_block[1].text) 
                        column_details.append(value_str) 
                        counter+=1
                    else :
                        column_details_name.append(td_block[0].text)
                        column_details_values.append(value_str)
        except:pass

    df = pd.DataFrame({'column_name':column_name,'column_description':column_description,'column_details':column_details}) 
    df['column_description'] = df['column_description'].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True)
        
    df_values = pd.DataFrame({'column_name':column_details_name,'column_values':column_details_values}) 
    df_values[['code','value']] = df_values["column_values"].str.split(" ", 1, expand=True)
    df_values = df_values[['column_name','code','value']]
    
    f.close()
    os.remove("saved_temp.html")
    
    return df, df_values

def download_metadata() :
    df_exports, df_values_exports = url_list_from_web(URL_METADATA_EXPORTACIONES)
    df_imports, df_values_imports = url_list_from_web(URL_METADATA_IMPORTACIONES)

    df_exports.to_csv(PATH+'columns_for_export_files.csv',encoding='utf-8-sig', index = False)
    df_imports.to_csv(PATH+'columns_for_import_files.csv',encoding='utf-8-sig', index = False)
    df_values_exports.to_csv(PATH+'values_for_export_files.csv',encoding='utf-8-sig', index = False)
    df_values_imports.to_csv(PATH+'values_for_import_files.csv',encoding='utf-8-sig', index = False)

def sync_data() :
    start_time = time.time()
    print("========================")
    print("START!!!")
    print("========================")
    df = get_list_of_files()
    download_new_data_from_dane(df)
    download_metadata()
    final_time = time.time()
    diff = (final_time - start_time)/60
    print("==================")
    print("Time:",diff,"min")
    print("END!!!")
    print("==================")
    
sync_data()