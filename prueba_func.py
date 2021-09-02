from controller import local_to_dataframes as ltd
import plotly.express as px
from controller import mari_controller as mc
import pandas as pd


df,df_exports=mc.lineplot(2,"Enero",2020,"Diciembre",2020,"","","")


df_exports["País destino"]=df_exports["País destino"].astype(int)

#df_imports["País origen"]=df_imports["País origen"].astype(int)
print("PRUEBAAAAAAAAAAAAAAAA")
print(df_imports.info())
print(df_imports.head(10))

