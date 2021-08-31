from controller import local_to_dataframes as ltd
import plotly.express as px
from controller import mari_controller as mc
import pandas as pd


def cargar_lineplot():
    df_exports_line=pd.read_csv("data/CSV/df_exports_grouped.csv")
    df_imports_line=pd.read_csv("data/CSV/df_imports_grouped.csv")
    #df_imports_line["Posición arancelaria"]=df_imports_line["Posición arancelaria"].astype(str)
    df_exports_line["Posición Arancelaria"]=df_exports_line["Posición Arancelaria"].astype(str)

    return df_exports_line,df_imports_line

df_exports_line,df_imports_line=cargar_lineplot()
print(df_exports_line.head(2))
print(df_exports_line.info())

print(df_imports_line.head(2))
print(df_imports_line.info())