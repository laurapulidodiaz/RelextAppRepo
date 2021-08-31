from controller import local_to_dataframes as ltd
import plotly.express as px
from controller import mari_controller as mc
import pandas as pd


def cargar_lineplot(FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH):

    MONTHS = ["Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio","Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    df_exports_line=pd.read_csv("data/CSV/df_exports_grouped.csv", low_memory=False)
    df_imports_line=pd.read_csv("data/CSV/df_imports_grouped.csv", low_memory=False)

    df_exports_line["Mes"] = pd.Categorical(df_exports_line["Mes"], categories=MONTHS, ordered=True)
    df_imports_line["Mes"] = pd.Categorical(df_imports_line["Mes"], categories=MONTHS, ordered=True)
    df_imports_line["Posición arancelaria"]=df_imports_line["Posición arancelaria"].astype(str)
    df_exports_line["Posición Arancelaria"]=df_exports_line["Posición Arancelaria"].astype(str)
    df_exports_line["Fecha"] = df_exports_line["Mes"].astype(str) + "-" + df_exports_line["Año"].astype(str)
    df_imports_line["Fecha"] = df_imports_line["Mes"].astype(str) + "-" + df_imports_line["Año"].astype(str)

    df_exports_line=df_exports_line[(df_exports_line["Mes"]>=FROM_MONTH) & (df_exports_line["Año"]>=FROM_YEAR_EXP)]
    df_exports_line = df_exports_line[(df_exports_line["Mes"] <= TO_MONTH) & (df_exports_line["Año"] >= TO_YEAR_EXP)]

    return df_exports_line,df_imports_line

df_exports_line,df_imports_line=cargar_lineplot(2019,"Enero",2019,"Diciembre")
print(df_exports_line.head(2))
print(df_exports_line.info())

print(df_imports_line.head(2))
print(df_imports_line.info())