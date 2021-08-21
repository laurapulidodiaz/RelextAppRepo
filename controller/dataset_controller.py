from controller import local_to_dataframes as ltd

def min_max_scale(x):
    x_max = x.max()
    x_min = x.min()
    if x_max == x_min:
        return x.apply(lambda z: 0)
    return x.apply(lambda z: (z-x_min)/(x_max-x_min))

def min_max_scaled(data, how='all'):
    min_max_scaled_df = data.copy()
    if how == 'row':
        return min_max_scaled(min_max_scaled_df.T, how='col').T
    elif how == 'all':
        x_max = min_max_scaled_df.max().max()
        x_min = min_max_scaled_df.min().min()
        return (min_max_scaled_df-x_min)/(x_max-x_min)
    else:
        for col in min_max_scaled_df.columns:
            min_max_scaled_df[col] = min_max_scale(min_max_scaled_df[col])
        return min_max_scaled_df

    

def loc_grouped(type, date_start=0, date_end=0):
    #TODO: definir date_start y date_end para convertirlos a el formato de la función
    if type=='exports':
        df_exports, _ = ltd.cargar_dataframes_export(2020, "Enero", 2020, "Enero")
        data = df_exports.groupby('Código país destino').sum()[['Total valor FOB doláres de la posición']].reset_index()
    elif type=='imports':
        df_imports, _ = ltd.cargar_dataframes_import(2020, "Enero", 2020, "Enero")
        data = df_imports.groupby('Código país origen').sum()[['Total valor FOB doláres de la posición']].reset_index()
    elif type=='balance':
        df_exports, df_imports, _, _ = ltd.cargar_dataframes(2020, "Enero", 2020, "Enero")
        data1 = df_exports.groupby('Código país destino').sum()[['Total valor FOB doláres de la posición']].reset_index()
        data2 = df_imports.groupby('Código país origen').sum()[['Total valor FOB doláres de la posición']].reset_index()
        data = data1['Total valor FOB doláres de la posición'].subtract(data2['Total valor FOB doláres de la posición'], fill_value=0)

    return data



    