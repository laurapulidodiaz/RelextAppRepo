import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import urllib.request
import csv
import os
import time

BASE_URL = "data/CSV"

TYPES = {
    "IMPORTS" : { "folder" : "Importaciones", "encoding" : "latin-1", "code": 0 },
    "EXPORTS" : { "folder" : "Exportaciones", "encoding" : "latin-1" , "code": 1 } }

MONTHS = ["Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio","Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

col_dict_exp={"Código país destino (numérico)": "País destino",
              "Código país destino (alfabético)": "Código país destino",
              "Código lugar de salida (alfabético)":"Código lugar de salida",
              "Código de la vía de transporte":"Vía de transporte",
              "Código modalidad de la exportación": "Modalidad de la exportación",
              "Código de la Aduana": "Aduana",
              "Código lugar de salida (numérico)":"Lugar de salida",
              "Forma de pago (1=Con reintegro 2=Sin reintegro)":"Forma de pago",
              "Tipo de certificado de origen (8 opciones)":"Tipo de certificado de origen",
              "Sistemas Especiales (1= Si 2= No)":"Sistemas especiales",
              "Departamento de origen por posición.":"Departamento de origen por posición"}

cat_dict_exp={"Aduana":"category", "Vía de transporte":"category",
         "Modalidad de la exportación":"category",
         "Forma de pago":"category", "Tipo de certificado de origen":"category",
          "Sistemas especiales": "category",
          "Código de unidad comercial de medida (numérico)":"category",
          "Código de unidad comercial de medida (alfabético)":"category",
              'Posición Arancelaria': 'str',
              'Código del regimen (acorde con CAN)': 'str',
              'Código de unidad comercial de medida (numérico)': 'str',
             "País destino":"str"}

replace_dict = {'137': 'Islas Caimán',
                '145': 'República Unida del Camerún',
                '177': 'Congo',
                '187': 'Corea del Norte',
                '190': 'Corea del Sur',
                '200': 'Checoslovaquia',
                '372': 'República Islámica del Irán',
                '469': 'Islas Marianas del Norte',
                '494': 'Estados Federados de Micronesia',
                '511': 'Islas Navidad',
                '631': 'ZFP Palermo',
                '633': 'ZFP FEMSA',
                '744': 'República Árabe de Siria',
                '756': 'República de Sudáfrica',
                '780': 'República Unia de Tanzania',
                '786': '786',
                '850': 'Venezuela',
                '863': 'Islas (Británicas) Vírgenes',
                '939': 'ZFP Intexzona',
                '940': 'ZFP Tayrona S.A.',
                '954': 'ZFP de Occidente',
                '960': 'ZFP de Tocancipa',
                '969': 'ZFPE Cencauca',
                '974': 'ZFP Metropolita',
                '979': 'ZFPE Productos',
                '989': 'ZFP Parque Central',
                "98":"Bonaire",
                "677":"Salomón, Islas",
                "420":"Laos, República",
                "501":"Montserrat, Islas",
                "535":"Norfolk, Isla",
               }

def load_metadata(selected_type):
    global BASE_URL
    dictionary_per_column = {}

    #URLS are fixed
    if selected_type["code"] == 0:
        URL_VALUES = f"{BASE_URL}/values_for_import_files.csv"
    else :
        URL_VALUES = f"{BASE_URL}/values_for_export_files.csv"

    with open(URL_VALUES, 'r', encoding="utf-8") as fr:
        lines = fr.readlines()

    dictionary_per_column['BANDERA'] = {}
    dictionary_per_column['ADUA'] = {}

    for line in lines :
        line = line.replace('\t','')
        line = line.replace('\n','')
        line = line.strip()
        line = line.replace('  ',' ')
        line = line.replace('  ',' ')
        line = line.replace('  ',' ')
        splitted_line = line.split(",")
        if len(splitted_line)==3 :
            column = splitted_line[0]
            column = column.replace('"','')
            if not column == 'column_name' :
                if not column in dictionary_per_column :
                    dictionary_per_column[column] = {}
                code = splitted_line[1]
                code = code.replace('"','')
                code = code.strip()
                value = splitted_line[2]
                value = value.replace('"','')
                value = value.strip()
                try :
                    code_number = int(code)
                    dictionary_per_column[column][code_number] = value
                except :
                    continue

                dictionary_per_column[column][code] = value

    #little fuckit hack
    dictionary_per_column['PAIS'] = dictionary_per_column['BANDERA']
    dictionary_per_column['COD_SAL1'] = dictionary_per_column['ADUA']
    dictionary_per_column['PAISGEN'] = dictionary_per_column['BANDERA']
    dictionary_per_column['PAISPRO'] = dictionary_per_column['BANDERA']
    fr.close()

    return dictionary_per_column

def get_index_from_month(month) :
    global MONTHS
    return MONTHS.index(month)

def load_dataframes(selected_type, initial_year, initial_month, last_year, last_month):
    global BASE_URL
    global MONTHS

    indice_mes_inicial = get_index_from_month(initial_month)
    indice_mes_final = get_index_from_month(last_month)

    data_aws_fulldf = pd.DataFrame()

    pd.options.display.max_columns = None
    start_time = time.time()
    folder = selected_type["folder"]

    print("========================")
    print("START!!!")
    print("========================")

    for year in range(initial_year, last_year+1):
        print("========================")
        print("Year: "+str(year))
        data_aws = pd.DataFrame()

        MONTHS_NEW = MONTHS

        if last_year == initial_year :
            MONTHS_NEW = MONTHS_NEW[indice_mes_inicial:(indice_mes_final+1)]
        elif initial_year == year :
            MONTHS_NEW = MONTHS_NEW[indice_mes_inicial:]
        elif last_year == year :
            MONTHS_NEW = MONTHS_NEW[:(indice_mes_final+1)]

        for month in MONTHS_NEW:
            print("Month: "+month)
            FILE_PATH = f"{BASE_URL}/{folder}/{year}/{month}.csv"
            dec=","
            try:
                with open(FILE_PATH, 'r', encoding=selected_type["encoding"]) as csvfile:
                    dialect = csv.Sniffer().sniff(csvfile.readline())
                    sep=dialect.delimiter
                    if sep==",":
                        dec="."

                data_aws_temp = pd.read_csv(FILE_PATH, float_precision='round_trip', sep=sep, decimal=dec, encoding=selected_type["encoding"], low_memory=False)
                data_aws_temp["Mes"]=month
                data_aws_temp["Año"]=year
                data_aws=data_aws.append(data_aws_temp, ignore_index=True)

            except:
                print("No existe el archivo: "+FILE_PATH)

        #Agregamos el dataframe al diccionario
        data_aws_fulldf = data_aws_fulldf.append(data_aws)

    final_time = time.time()
    diff = (final_time - start_time)/60

    print("========================")
    print("COMPLETED!!!")
    print("Time:",diff,"min")
    print("========================")
    return data_aws_fulldf

def update_metadata_in_dataframe(data_aws_fulldf_b, dictionary_per_column) :
    print("========================")
    print("Start Update")
    start_time = time.time()
    data_aws_fulldf_c = data_aws_fulldf_b.replace(dictionary_per_column)
    final_time = time.time()
    diff = (final_time - start_time)/60
    print("========================")
    print("Time Update:",diff,"min")
    return data_aws_fulldf_c

# load full description headers
def load_headers(selected_type):
    global BASE_URL
    headers = {}

    #URLS are fixed
    if selected_type["code"] == 0:
        URL_COLUMNS = f"{BASE_URL}/columns_for_import_files.csv"
    else :
        URL_COLUMNS = f"{BASE_URL}/columns_for_export_files.csv"

    with open(URL_COLUMNS, 'r', encoding="utf-8") as fr:
        lines = fr.readlines()

    for line in lines :
        line = line.replace('\t','')
        line = line.replace('\n','')
        line = line.strip()
        line = line.replace('  ',' ')
        line = line.replace('  ',' ')
        line = line.replace('  ',' ')
        splitted_line = line.split(",")
        if len(splitted_line)==3 :
            column = splitted_line[0]
            column = column.replace('"','')
            if not column == 'column_name' :
                description = splitted_line[1]
                description = description.replace('"','')
                description = description.strip()
                headers[column] = description
    fr.close()
    return headers

# update dataframe with full description headers
def update_df_headers(df, headers):
    df_new = df.rename(columns = headers)
    return df_new

def load_all_data(type_sel, INIT_YEAR, INIT_MONTH, FINAL_YEAR, FINAL_MONTH) :
    print("========================")
    print("LOADS DATA")
    data_aws_fulldf = load_dataframes(TYPES[type_sel], INIT_YEAR, INIT_MONTH, FINAL_YEAR, FINAL_MONTH)
    print("========================")
    print("LOADS METADATA")
    dictionary_per_column = load_metadata(TYPES[type_sel])
    res = next(iter(dictionary_per_column))
    print(str(res))
    print("========================")
    print("UPDATE DATA FROM META")
    data_aws_fulldf_a = update_metadata_in_dataframe(data_aws_fulldf, dictionary_per_column)
    print("========================")
    print("UPDATE HEADERS")
    headers = load_headers(TYPES[type_sel])
    data_aws_fulldf_a = update_df_headers(data_aws_fulldf_a, headers)
    print("========================")
    print("THE END!!!")
    print("========================")

    return data_aws_fulldf_a

def pruebas(type_sel, INIT_YEAR, INIT_MONTH, FINAL_YEAR, FINAL_MONTH) :
    print("========================")
    print("LOADS DATA")
    data_aws_fulldf = load_dataframes(TYPES[type_sel], INIT_YEAR, INIT_MONTH, FINAL_YEAR, FINAL_MONTH)
    print("========================")
    print("LOADS METADATA")
    dictionary_per_column = load_metadata(TYPES[type_sel])
    res = next(iter(dictionary_per_column))
    print(str(res))
    print("========================")
    print("UPDATE DATA FROM META")
    data_aws_fulldf_a = update_metadata_in_dataframe(data_aws_fulldf, dictionary_per_column)
    print("========================")
    print("UPDATE HEADERS")
    headers = load_headers(TYPES[type_sel])
    data_aws_fulldf_a = update_df_headers(data_aws_fulldf_a, headers)
    print("========================")
    print("THE END!!!")
    print("========================")

    return data_aws_fulldf


def cargar_data_arancel() :
    data_arancel = pd.read_excel(BASE_URL+'/Subpartidas/ARANCEL.xlsx', skiprows=[0,1,2], usecols="A,C,M")
    data_arancel.drop_duplicates(subset=["Subpartida Arancelaria"], inplace=True)

    return data_arancel

def cargar_dataframe_exportacion(data_arancel, FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH) :
    print("Cargando datos de exportación, desde",FROM_MONTH,"de",FROM_YEAR_EXP,"hasta",TO_MONTH,"de",TO_YEAR_EXP)
    df_exports = load_all_data("EXPORTS", FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH)
    try :
        df_exports = df_exports.merge( data_arancel, how = "left", left_on='Posición Arancelaria', right_on='Subpartida Arancelaria')
        df_exports = df_exports.drop(columns = ["Subpartida Arancelaria"])
        df_exports["Fecha"]=df_exports["Mes"]+"-"+df_exports["Año"].astype(str)

    except :
        pass
    return df_exports

def cargar_dataframe_importacion(data_arancel, FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH) :
    print("Cargando datos de importación, desde",FROM_MONTH,"de",FROM_YEAR_EXP,"hasta",TO_MONTH,"de",TO_YEAR_EXP)
    df_imports = load_all_data("IMPORTS", FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH)
    try :
        df_imports = df_imports.merge( data_arancel, how = "left", left_on='Posición arancelaria', right_on='Subpartida Arancelaria')
        df_imports = df_imports.drop(columns = ["Subpartida Arancelaria" ])
        df_imports = df_imports.drop(columns = ["Fecha de proceso" ])
        df_imports = df_imports.astype({'Posición arancelaria': 'str', 'Ciudad del importador': 'str'})
        df_imports["Fecha"] = df_imports["Mes"] + "-" + df_imports["Año"].astype(str)

    except:
        pass
    return df_imports

def cargar_dataframe_exportacion_cundinamarca(df_exports) :
    try :
        df_exports_cundinamarca = df_exports[df_exports["Departamento de procedencia"]==25]
        return df_exports_cundinamarca
    except :
        return 0

def cargar_dataframe_importacion_cundinamarca(df_imports) :
    try :
        df_imports_cundinamarca = df_imports[df_imports["Departamento destino"]==25]
        return df_imports_cundinamarca
    except :
        return 0

def ejecutar_datacleaning_exports(df_exports) :
    global replace_dict
    global col_dict_exp
    global cat_dict_exp
    global MONTHS

    try :
        df_exports['Código país destino (numérico)'].replace(replace_dict, inplace=True)
        df_exports.rename(columns=col_dict_exp, inplace=True)
        df_exports=df_exports.astype(cat_dict_exp)
        df_exports["Mes"]=pd.Categorical(df_exports["Mes"],categories=MONTHS, ordered=True)
        df_exports['País destino'] = df_exports['País destino'].apply(lambda x: str(x))
        df_exports['País destino'].replace(replace_dict, inplace=True)
        df_exports["Departamento de procedencia"] = df_exports["Departamento de procedencia"].astype(int)

    except :
        pass

    return df_exports

def ejecutar_datacleaning_imports(df_imports) :
    global replace_dict
    global col_dict_exp
    global cat_dict_exp
    global MONTHS

    try :
        df_imports['País de procedencia'].replace(replace_dict, inplace=True)
        df_imports['País de compra'].replace(replace_dict, inplace=True)
        df_imports['País de procedencia'] = df_imports['País de procedencia'].apply(lambda x: str(x))
        df_imports['País de compra'] = df_imports['País de compra'].apply(lambda x: str(x))
        df_imports['País de procedencia'].replace(replace_dict, inplace=True)
        df_imports['País de compra'].replace(replace_dict, inplace=True)
        df_imports["Departamento destino"] = df_imports["Departamento destino"].astype(int)

    except :
        pass

    return df_imports

def cargar_dataframes_export(FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH) :
    data_arancel = cargar_data_arancel()
    df_exports = cargar_dataframe_exportacion(data_arancel, FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH)
    df_exports = ejecutar_datacleaning_exports(df_exports)
    df_exports_cundinamarca = cargar_dataframe_exportacion_cundinamarca(df_exports)

    return df_exports, df_exports_cundinamarca

def cargar_dataframes_import(FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH) :
    data_arancel = cargar_data_arancel()
    df_imports = cargar_dataframe_importacion(data_arancel, FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH)
    df_imports = ejecutar_datacleaning_imports(df_imports)
    df_imports_cundinamarca = cargar_dataframe_importacion_cundinamarca(df_imports)

    return df_imports, df_imports_cundinamarca

def cargar_dataframes(FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH) :
    data_arancel = cargar_data_arancel()
    df_imports = cargar_dataframe_importacion(data_arancel, FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH)
    df_exports = cargar_dataframe_exportacion(data_arancel, FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH)
    df_exports = ejecutar_datacleaning_exports(df_exports)
    df_imports = ejecutar_datacleaning_imports(df_imports)

    df_imports_cundinamarca = cargar_dataframe_importacion_cundinamarca(df_imports)
    df_exports_cundinamarca = cargar_dataframe_exportacion_cundinamarca(df_exports)

    return df_exports, df_imports, df_exports_cundinamarca, df_imports_cundinamarca

#def dataframes_pais(df_exports,df_imports,PAIS)




    #return

# Ejemplo de uso
# df_exports, df_imports, df_exports_cundinamarca, df_imports_cundinamarca = cargar_dataframes(2020, "Enero", 2020, "Enero")
# df_imports, df_imports_cundinamarca = cargar_dataframes_import(2020, "Enero", 2020, "Enero")
# df_exports, df_exports_cundinamarca = cargar_dataframes_export(2020, "Enero", 2020, "Enero")
