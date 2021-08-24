# Imports
from controller import local_to_dataframes as ltd
import plotly.express as px

#category= "Carbón coque y semicoque, carbón de lignito o carbón de hulla; carbón de retorta; alquitrán de carbón, de carbón lignito, hulla y otras tortas minerales"

# Barplots
def barplot_10_top(data = 1, country = "USA", department = 25, unit = "quantity", category = "",
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
        if category != "":
            df_filtered = df_filtered[df_filtered['Descriptiva - SCN - NUEVA BASE 2015'] == category]
        if country != "":
            df_filtered = df_filtered[df_filtered["Código país destino"] == country]
        if unit == "quantity":
            # Data to plot
            condition = df_filtered['Código de unidad comercial de medida (alfabético)'] == 'U'
            df_plot = df_filtered[condition].groupby('Descripción Arancelaria Corta')[['Cantidad de unidades de la posición']]
            df_plot = df_plot.sum().sort_values(by='Cantidad de unidades de la posición', ascending=False).reset_index().head(10)
            # Barplot
            fig = px.bar(df_plot, x='Cantidad de unidades de la posición', y='Descripción Arancelaria Corta')
        elif unit == "dollars":
            # Data to plot
            df_plot = df_filtered.groupby('Descripción Arancelaria Corta')[["Total valor FOB doláres de la posición"]].sum()
            df_plot = df_plot.sort_values(by='Total valor FOB doláres de la posición', ascending=False).reset_index().head(10)
            # Barplot
            fig = px.bar(df_plot, x='Total valor FOB doláres de la posición', y='Descripción Arancelaria Corta')
        elif unit == "pesos":
            # Data to plot
            df_plot = df_filtered.groupby('Descripción Arancelaria Corta')[["Total valor FOB pesos de la posición"]].sum()
            df_plot = df_plot.sort_values(by='Total valor FOB pesos de la posición', ascending=False).reset_index().head(10)
            fig = px.bar(df_plot, x='Total valor FOB pesos de la posición', y='Descripción Arancelaria Corta')

    # For dataset of imports
    elif data == 2:
        # Adjusting character values
        df_imports['Descripción Arancelaria'] = df_imports['Descripción Arancelaria'].astype(str)
        df_imports['Descripción Arancelaria Corta'] = df_imports['Descripción Arancelaria'].apply(lambda x: x[:50])
        # Filtering data
        if department is not None:
            df_filtered = df_imports[df_imports['Departamento destino'] == department]
        else:
            df_filtered = df_imports
        if category != "":
            df_filtered = df_filtered[df_filtered["Descriptiva - SCN - NUEVA BASE 2015"] == category]
        if country != "":
            df_filtered = df_filtered[df_filtered['País de procedencia'] == country]
        if unit == "quantity":
            # Data to plot
            condition = df_filtered['Código de unidad'] == 'U'
            df_plot = df_filtered[condition].groupby('Descripción Arancelaria Corta')[['Cantidad de unidades']]
            df_plot = df_plot.sum().sort_values(by='Cantidad de unidades', ascending=False).reset_index().head(10)
            # Barplot
            fig = px.bar(df_plot, x='Cantidad de unidades', y='Descripción Arancelaria Corta')
        elif unit == "dollars":
            # Data to plot
            df_plot = df_filtered.groupby('Descripción Arancelaria Corta')[["Valor CIF dólares de la mercancía"]].sum()
            df_plot = df_plot.sort_values(by='Valor CIF dólares de la mercancía', ascending=False).reset_index().head(10)
            # Barplot
            fig = px.bar(df_plot, x='Valor CIF dólares de la mercancía', y='Descripción Arancelaria Corta')
        elif unit == "pesos":
            # Data to plot
            df_plot = df_filtered.groupby('Descripción Arancelaria Corta')[["Valor CIF pesos de la mercancía"]].sum()
            df_plot = df_plot.sort_values(by='Valor CIF pesos de la mercancía', ascending=False).reset_index().head(10)
            # Barplot
            fig = px.bar(df_plot, x='Valor CIF pesos de la mercancía', y='Descripción Arancelaria Corta')

    return fig


# Histograms

def make_histogram(data, country, department, category = "", product ="", year_start = 2021, month_start= "Mayo",
                   year_end = 2021, month_end = "Mayo", unit = "quantity"):
    df_exports, df_imports, df_exports_cundinamarca, df_imports_cundinamarca = ltd.cargar_dataframes(year_start,
                                                                                                     month_start,
                                                                                                     year_end,
                                                                                                     month_end)
    if data == 1:
        # Filtering data
        if department is not None:
            df_filtered = df_exports[df_exports['Departamento de procedencia'] == department]
        else:
            df_filtered = df_exports
        if category != "":
            df_filtered = df_filtered[df_filtered['Descriptiva - SCN - NUEVA BASE 2015'] == category]
        if product != "":
            df_filtered = df_filtered[df_filtered['Descripción Arancelaria'] == product]
        if country != "":
            df_filtered = df_filtered[df_filtered["Código país destino"] == country]
        if unit =="quantity":
            fig = px.histogram(df_filtered, x='Cantidad de unidades de la posición', nbins=1000)
        elif unit == "dollars":
            fig = px.histogram(df_filtered, x='Total valor FOB doláres de la posición', nbins=1000)
        elif unit == "pesos":
            fig = px.histogram(df_filtered, x='Total valor FOB pesos de la posición', nbins=1000)

    elif data == 2:
        # Filtering data
        if department is not None:
            df_filtered = df_imports[df_imports['Departamento destino'] == department]
        else:
            df_filtered = df_imports
        if category != "":
            df_filtered = df_filtered[df_filtered['Descriptiva - SCN - NUEVA BASE 2015'] == category]
        if product != "":
            df_filtered = df_filtered[df_filtered['Descripción Arancelaria'] == product]
        if country != "":
            df_filtered = df_filtered[df_filtered['País de procedencia'] == country]
        if unit =="quantity":
            # Histogram
            fig = px.histogram(df_filtered, x='Cantidad de unidades', nbins=1000)
        elif unit == "dollars":
            fig = px.histogram(df_filtered, x='Valor CIF dólares de la mercancía', nbins=1000)
        elif unit == "pesos":
            fig = px.histogram(df_filtered, x='Valor CIF dólares de la mercancía', nbins=1000)

    return fig