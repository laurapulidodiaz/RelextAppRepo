# Imports
import numpy as np
import pandas as pd
from controller import local_to_dataframes as ltd
import plotly.express as px

# Function to create Barplots for the top 10 products according to the user inputs
# This is shown in the tab 'Productos TOP'
def barplot_10_top(data, country, department, year_start, month_start, year_end, month_end):
    if country == None:
        country = ""
    if department == None:
        department = ""
    if year_start == None:
        year_start = 2021
    if month_start == None:
        month_start = "Mayo"
    if year_end == None:
        year_end = 2021
    if month_end == None:
        month_end = "Mayo"

    POS = ""
    # Loading exports and imports data filtered according to inputs
    df_exports, df_imports = ltd.dataframes_all_filtros(year_start, month_start, year_end, month_end, country,
                                                        department, POS)

    # For dataset of exports
    if data == 1:
        # Adjusting character values
        df_exports['Descripción Arancelaria'] = df_exports['Descripción Arancelaria'].astype(str)
        df_exports['Descripción Arancelaria Corta'] = df_exports['Descripción Arancelaria'].apply(lambda x: x[:50])
        print(df_exports.head(2))
        # Data to plot
        df_plot = df_exports.groupby('Descripción Arancelaria Corta')[["Total valor FOB doláres de la posición"]].sum()
        df_plot = df_plot.sort_values(by='Total valor FOB doláres de la posición', ascending=False).reset_index().head(
            10)
        print("PLOOOOT", df_plot.head(2))
        # Barplot
        fig = px.bar(df_plot, x='Total valor FOB doláres de la posición', y='Descripción Arancelaria Corta')
    # For dataset of imports
    elif data == 2:
        # Adjusting character values
        df_imports['Descripción Arancelaria'] = df_imports['Descripción Arancelaria'].astype(str)
        df_imports['Descripción Arancelaria Corta'] = df_imports['Descripción Arancelaria'].apply(lambda x: x[:50])

        # Data to plot
        df_plot = df_imports.groupby('Descripción Arancelaria Corta')[["Valor CIF dólares de la mercancía"]].sum()
        df_plot = df_plot.sort_values(by='Valor CIF dólares de la mercancía', ascending=False).reset_index().head(10)
        # Barplot
        fig = px.bar(df_plot, x='Valor CIF dólares de la mercancía', y='Descripción Arancelaria Corta')
    # For production

    elif data == 3:
        # Reading production data
        df_prod = pd.read_csv('./data/CSV/SIPRA_2019_2020_unificado.csv', sep = ";", low_memory=False)
        # Filtering data
        if department != "":
            df_prod = df_prod[df_prod['Codigo del departamento']==department]
        # Organizing data to plot
        df_plot = df_prod.groupby('Cultivo').sum()['Area Cosechada (ha)'].reset_index()
        df_plot = df_plot.sort_values(by='Area Cosechada (ha)', ascending=False).head(10)
        # Barplot
        fig = px.bar(df_plot, x='Area Cosechada (ha)', y='Cultivo')

    return fig


# Function to create Histograms of the value of transactions
# This is shown in the tab 'Gráficos de Distribución'

def make_histogram(data, country, department, product, year_start, month_start,
                   year_end, month_end):
    global fig
    if country == None:
        country = ""
    if department == None:
        department = ""
    if year_start == None:
        year_start = 2021
    if month_start == None:
        month_start = "Mayo"
    if year_end == None:
        year_end = 2021
    if month_end == None:
        month_end = "Mayo"
    if product == None:
        product = ""
    # Loading data filtered according to inputs
    df_exports, df_imports = ltd.dataframes_all_filtros(year_start, month_start, year_end, month_end, country,
                                                        department, product)
    # For exports datasets
    if data == 1:
        df = df_exports
        # Setting values into a logarithmic scale
        df['Log. Valor FOB USD'] = np.log(df['Total valor FOB doláres de la posición'])
        # Creating histogram
        fig = px.histogram(df, x='Log. Valor FOB USD', nbins=1000)

    # For imports datasets
    elif data == 2:
        df = df_imports
        # Setting values into a logarithmic scale
        df['Log. Valor CIF USD'] = np.log(df['Valor CIF dólares de la mercancía'])
        # Creating histogram
        fig = px.histogram(df_imports, x='Log. Valor CIF USD', nbins=1000)

    return fig