# Imports
from controller import local_to_dataframes as ltd
import plotly.express as px
from controller import consulta_controller as cons
import plotly.graph_objects as go

#category= "Carbón coque y semicoque, carbón de lignito o carbón de hulla; carbón de retorta; alquitrán de carbón, de carbón lignito, hulla y otras tortas minerales"

# Barplots
def barplot_10_top(data, country, department, year_start, month_start,year_end, month_end):
    if country == None:
        country=249
    if department==None:
        department=25
    if year_start==None:
        year_start=2021
    if month_start==None:
        month_start="Mayo"
    if year_end==None:
        year_end=2021
    if month_end==None:
        month_end="Mayo"

    print("pruebaaa Juli", country, department)
    POS=""
    df_exports,df_imports=ltd.dataframes_all_filtros(year_start, month_start,year_end,month_end,country,department, POS)

    # For dataset of exports
    if data == 1:
        # Adjusting character values
        df_exports['Descripción Arancelaria'] = df_exports['Descripción Arancelaria'].astype(str)
        df_exports['Descripción Arancelaria Corta'] = df_exports['Descripción Arancelaria'].apply(lambda x: x[:50])
        print(df_exports.head(2))
        # Data to plot
        df_plot = df_exports.groupby('Descripción Arancelaria Corta')[["Total valor FOB doláres de la posición"]].sum()
        df_plot = df_plot.sort_values(by='Total valor FOB doláres de la posición', ascending=False).reset_index().head(10)
        print("PLOOOOT",df_plot.head(2))
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

    return fig
#
    # Histograms

def make_histogram(data, country, department, product, year_start, month_start,
                   year_end, month_end ):
    if country == None:
        country=249
    if department==None:
        department=25
    if year_start==None:
        year_start=2021
    if month_start==None:
        month_start="Mayo"
    if year_end==None:
        year_end=2021
    if month_end==None:
        month_end="Mayo"

    df_exports, df_imports = ltd.dataframes_all_filtros(year_start, month_start, year_end, month_end, country,
                                                        department, product)
    if data == 1:

        fig = px.histogram(df_exports, x='Total valor FOB doláres de la posición', nbins=1000)


    elif data == 2:

        fig = px.histogram(df_imports, x='Valor CIF dólares de la mercancía', nbins=1000)

    return fig

# Barplot balanza comercial
def balanza_bp(product = "", year_start = 2021, month_start= "Mayo", year_end = 2021, month_end = "Mayo"):
    df_balanza = cons.balanza_producto(year_start, month_start, year_end, month_end)
    if product != "":
        df_filtered = df_balanza[df_balanza['Descripción Arancelaria'] == product]
    else:
        df_filtered = df_balanza

    #fig = go.Figure()
    #fig.add_trace(go.Bar(x = df_filtered['Descripción Arancelaria'], y = df_filtered['Total Exportaciones'], name='Exportaciones'))
    #fig.add_trace(go.Bar(x = df_filtered['Descripción Arancelaria'], y = df_filtered['Total Importaciones'], name='Importaciones'))
    fig = go.Figure(data=[
        go.Bar(x = df_filtered['Descripción Arancelaria'], y = df_filtered['Total Exportaciones'],
                      name='Exportaciones'),
        go.Bar(x = df_filtered['Descripción Arancelaria'], y = df_filtered['Total Importaciones'],
               name='Importaciones')
    ]).update_layout(barmode='group')

    return fig