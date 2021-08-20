from controller import local_to_dataframes as ltd
from datetime import datetime
from controller.local_to_dataframes import MONTHS

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
        df_exports_cundinamarca['Descripción Arancelaria'] = df_exports['Descripción Arancelaria'].astype(str)
        df_exports_cundinamarca['Descripción Arancelaria Corta'] = df_exports['Descripción Arancelaria'].apply(lambda x : x[:100])
        df = df_exports_cundinamarca.groupby("Descripción Arancelaria Corta").sum()[["Total valor FOB doláres de la posición"]].reset_index()
        df = df.sort_values(by=["Total valor FOB doláres de la posición"], ascending=False).head(10)

        return df, year_selected, month_selected
