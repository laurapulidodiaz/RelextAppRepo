
from controller import local_to_dataframes as ltd

#df_exports, df_imports,_,_=ltd.cargar_dataframes(2021, "Mayo", 2021, "Mayo")
PAIS=11
DPTO=""
POS=""
CAT=""

df_exp,df_imp=ltd.dataframes_all_filtros(2021, "Mayo", 2021, "Mayo",PAIS, DPTO, POS, CAT)
print(df_exp.head(2))