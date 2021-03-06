from controller import local_to_dataframes as ltd
from datetime import datetime
from controller.local_to_dataframes import MONTHS
import pandas as pd
import json
pd.options.mode.chained_assignment = None

def get_two_months_ago() :
    year_selected = datetime.today().year
    month_selected = datetime.today().month

    if month_selected > 3 :
        month_selected = MONTHS[month_selected-4]
    else :
        year_selected = year_selected - 1
        month_selected = MONTHS[month_selected-4+12]

    return year_selected, month_selected

def data_cundinamarca_top10_export() :
    year_selected, month_selected = get_two_months_ago()
    df_exports, df_exports_cundinamarca = ltd.cargar_dataframes_export(year_selected, month_selected, year_selected, month_selected)

    if type(df_exports_cundinamarca) == int :
        return 0, year_selected, month_selected
    else :
        df_exports_cundinamarca['Descripción Arancelaria'] = df_exports_cundinamarca['Descripción Arancelaria'].astype(str)
        df_exports_cundinamarca['Descripción Arancelaria Corta'] = df_exports_cundinamarca['Descripción Arancelaria'].apply(lambda x : x[:100])
        df = df_exports_cundinamarca.groupby("Descripción Arancelaria Corta").sum()[["Total valor FOB doláres de la posición"]].reset_index()
        df = df.sort_values(by=["Total valor FOB doláres de la posición"], ascending=False).head(10)

        return df, year_selected, month_selected

def get_ISO_alpha(pais, data):
    try:
        return data[data['Nombre del país'] == pais]['ISO_alpha_3'].iloc[0]
    except:
        return pais

def loc_grouped(anoini=2021, mesini='Mayo', anofin=2021, mesfin='Mayo'):
    '''
    Devuelve 3 dataframes agrupados por país: exports, imports y balance.
    Estos dataframes tienen 2 columnas: 'País' y 'Valor FOB dólares de la mercancía'
    '''

    rename_dict = { 'Código país destino': 'País',
                    'Total valor FOB doláres de la posición':'Valor FOB dólares de la mercancía',
                    'País origen': 'País',}

    df_exports, df_imports, cund, cund_ = ltd.cargar_dataframes(FROM_YEAR_EXP = anoini, FROM_MONTH = mesini, TO_YEAR_EXP = anofin, TO_MONTH = mesfin)

    ISO = pd.read_csv("data/CSV/ISO_alpha.csv")


    if type(cund) == int or type(cund_) == int:
        return 0, 0
    else:
        df_exports = df_exports.groupby('Código país destino').sum()[['Total valor FOB doláres de la posición']].reset_index().rename(columns=rename_dict)
        df_imports = df_imports.groupby('País origen').sum()[['Valor FOB dólares de la mercancía']].reset_index().rename(columns=rename_dict)

        df_imports['País'] = df_imports['País'].apply(lambda x: get_ISO_alpha(x, ISO))


        return df_exports, df_imports

def balanza_producto(year_start, month_start, year_end, month_end):
    df_exports, df_imports, _a, _b = ltd.cargar_dataframes(year_start, month_start, year_end, month_end)
    df_balanza = df_imports.merge(df_exports, how='full', on='Descripción Arancelaria')
    df_balanza = df_balanza.groupby('Descripción Arancelaria').sum()[['Total valor FOB doláres de la posición', 'Valor CIF dólares de la mercancía']].reset_index()
    df_balanza = df_balanza.rename({'Total valor FOB doláres de la posición': 'Total Exportaciones',
                                    'Valor CIF dólares de la mercancía': 'Total Importaciones'})
    return df_balanza

