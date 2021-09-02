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

#print(df_exports["País destino"].value_counts().sort_values(ascending=True)[0:100])
#df_imports["País destino"]=df_exports["País destino"].replace(paises_dict)
#df_exports["País destino"]=df_exports["País destino"].astype(int)


df_imports["País origen"]=df_imports["País origen"].replace(paises_dict)
df_imports["País origen"]=df_imports["País origen"].astype(int)
print("PRUEBAAAAAAAAAAAAAAAA")
print(df_exports.info())
print(df_exports.head(10))


