
from controller import local_to_dataframes as ltd

df_exports, df_imports,_,_=ltd.cargar_dataframes(2021, "Mayo", 2021, "Mayo")
#print(df_exports.head(2),df_exports.info())
print(df_exports.info())
#print(df_imports.head(2))
print(df_imports.info())


def dataframes_pais(df_exports,df_imports,PAIS):
	df_exports=df_exports[df_exports["País destino"]==PAIS]
	df_imports=df_imports[df_imports["País origen"]==PAIS]

	return df_exports,df_imports


def dataframes_dpto(df_exports, df_imports, DPTO):
    df_exports = df_exports[df_exports["Departamento de origen por posición"] == DPTO]
    df_imports = df_imports[df_imports["Departamento del importador"] == DPTO]

    return df_exports, df_imports

df_exports, df_imports=dataframes_dpto(df_exports, df_imports, 11)

print(df_exports.tail(2))
print(df_imports.tail(2))

def dataframes_pos(df_exports,df_imports,POS)
	"""
	POS string"""

	df_exports=df_exports[df_exports["Posición Arancelaria"]==POS]
	df_imports=df_imports[df_imports["Posición arancelaria"]==POS]

	return df_exports, df_imports

def dataframes_CAT(df_exports,df_imports, CAT)
	""" 
	CAT string"""
	df_exports=df_exports[df_exports["SCN - BASE 2015"]==CAT]
	df_imports=df_imports[df_imports["SCN - BASE 2015"]==CAT]

	return df_exports,df_imports


no borrar la columna de categoria
