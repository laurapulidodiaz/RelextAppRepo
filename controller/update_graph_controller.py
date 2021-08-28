import plotly.express as px
import plotly.graph_objects as go
from controller import local_to_dataframes as ltd
from controller import consulta_controller as conc

def update_choropleth_world(tipo=1, anoini=2021, mesini='Mayo', anofin=2021, mesfin='Mayo'):

    dataframes = conc.loc_grouped(anoini, mesini, anofin, mesfin)

    if tipo<=3:
        dff = dataframes[tipo - 1]

    fig = go.Figure(data=go.Choropleth(
        locations=dff['País'],
        z=dff['Valor FOB dólares de la mercancía'],
        text=dff['País'],
        colorscale='Blues',
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix='$',
        # colorbar_title = 'GDP<br>Billions US$',
    ))

    return fig

def update_heatmap(tipo=1, anoini=2021, mesini='Mayo', anofin=2021, mesfin='Mayo'):
    col_x = 'Código país destino'
    col_y = 'Descriptiva - SCN - NUEVA BASE 2015'
    col_z = 'Total valor FOB doláres de la posición'
    n_rows = 30
    n_cols = 20

    df_exports, df_imports = ltd.cargar_dataframes_export(anoini, mesini, anofin, mesfin)

    mini_df = df_exports.groupby([col_x, col_y])[[col_z]].sum().unstack(level=-1)
    #flatten columns, resultan en 2 niveles al hacer unstack
    mini_df.columns = [y for x, y in mini_df.columns.values]

    top_columns = mini_df.sum().sort_values(ascending=False).head(n_cols).index
    top_rows = df_exports.groupby(col_x)[col_z].sum().sort_values(
        ascending=False).head(n_rows).index

    #Labels deben cambiar al definir los inputs
    fig = px.imshow(
        mini_df[top_columns].loc[top_rows],
        labels=dict(x="Producto", y="País", color="Valor FOB"),
    )

    axis_template = dict(
        linecolor='black', showticklabels=False,
        ticks=''
    )

    fig.update_layout(
        xaxis=axis_template, )

    return fig