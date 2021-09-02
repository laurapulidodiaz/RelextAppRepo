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

df,df_exports=mc.lineplot(2,"Enero",2020,"Diciembre",2020,"","","")

df_exports["Departamento de origen por posición"] = df_exports["Departamento de origen por posición"].replace({' ':0}).astype(int)

print("PRUEBAAAAAAAAAAAAAAAA")
print(df_exports.info())
print(df_exports.head(10))


