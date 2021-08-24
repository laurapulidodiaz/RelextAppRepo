# Imports
from controller import local_to_dataframes as ltd
import plotly.express as px
import pandas as pd
#category= "Carbón coque y semicoque, carbón de lignito o carbón de hulla; carbón de retorta; alquitrán de carbón, de carbón lignito, hulla y otras tortas minerales"
# Barplots
def barplot_10_top(data = 1, country = "USA", department = 25,
                   year_start = 2020, month_start= "Enero", year_end = 2020, month_end = "Enero"):
    df_exports, df_imports, df_exports_cundinamarca, df_imports_cundinamarca = ltd.cargar_dataframes(year_start, month_start,
                                                                                                     year_end, month_end)
    # For dataset of exports
    if data == 1:
        # Adjusting character values
        df_exports['Descripción Arancelaria'] = df_exports['Descripción Arancelaria'].astype(str)
        df_exports['Descripción Arancelaria Corta'] = df_exports['Descripción Arancelaria'].apply(lambda x: x[:50])
        # Filtering data
        if department is not None:
            df_filtered = df_exports[df_exports['Departamento de procedencia'] == department]
        else:
            df_filtered = df_exports
        #if category != "":
        #    df_filtered = df_filtered[df_filtered['Descriptiva - SCN - NUEVA BASE 2015'] == category]
        if country != "":
            df_filtered = df_filtered[df_filtered["Código país destino"] == country]

        # Data to plot
        condition = df_filtered['Código de unidad comercial de medida (alfabético)'] == 'U'
        df_plot = df_filtered[condition].groupby('Descripción Arancelaria Corta')[['Cantidad de unidades de la posición']]
        df_plot = df_plot.sum().sort_values(by='Cantidad de unidades de la posición', ascending=False).reset_index().head(10)

        # Barplot
        fig = px.bar(df_plot, x='Cantidad de unidades de la posición', y='Descripción Arancelaria Corta')

    # For dataset of imports
    elif data == 2:
        # Adjusting character values
        df_imports['Descripción Arancelaria'] = df_imports['Descripción Arancelaria'].astype(str)
        df_imports['Descripción Arancelaria Corta'] = df_imports['Descripción Arancelaria'].apply(lambda x: x[:50])
        # Filtering data
        if department is not None:
            df_filtered = df_imports[df_imports['Departamento destino'] == department]
        else:
            df_filtered = df_exports
        #if category != "":
        #    df_filtered = df_filtered[df_filtered["Descriptiva - SCN - NUEVA BASE 2015"] == category]
        if country != "":
            df_filtered = df_filtered[df_filtered['País de procedencia'] == country]

        # Data to plot
        condition = df_filtered['Código de unidad'] == 'U'
        df_plot = df_filtered[condition].groupby('Descripción Arancelaria Corta')[['Cantidad de unidades']]
        df_plot = df_plot.sum().sort_values(by='Cantidad de unidades', ascending=False).reset_index().head(10)

        # Barplot
        fig = px.bar(df_plot, x='Cantidad de unidades', y='Descripción Arancelaria Corta')

    return fig


