
from controller import local_to_dataframes as ltd

df_exports, df_imports,_,_=ltd.cargar_dataframes(2017, "Enero", 2021, "Mayo")
print(df_exports.head(2))
print(df_exports.info())
print(df_imports.head(2))
print(df_imports.info())


