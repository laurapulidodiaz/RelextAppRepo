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

df=mc.lineplot(1,"Enero",2020,"Mayo",2020,"","","")
df.drop(index=df.index[df["Total valor FOB doláres de la posición"]==0], inplace=True)

print("PRUEBAAAAAAAAAAAAAAAA")
print(df["Mes"].value_counts())
print(df.info())


