from controller import local_to_dataframes as ltd
import plotly.express as px
from controller import mari_controller as mc
import pandas as pd


def dict_paises():
    paises = pd.read_csv("data/CSV/paisesall.csv", low_memory=False, delimiter=";").set_index("value")
    paises_dict = paises.to_dict()
    paises_dict = paises_dict["code"]

    return paises_dict


paises_dict=dict_paises()

df,df_imports=mc.lineplot(2,"Enero",2020,"Diciembre",2020,"","","")

df_imports["Departamento del importador"] = df_imports["Departamento del importador"].astype(int)

print("PRUEBAAAAAAAAAAAAAAAA")
print(df_imports.info())
print(df_imports.head(10))


