import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from controller import update_graph_controller as ugc

def cargar_geo(tipo=1,pais="",dpto="",pos="",cat="",mesini='Mayo',anoini=2021,mesfin='Mayo',anofin=2021):
    #Exportaciones Mayo 2021 a Mayo 2021
    grafico= ugc.update_choropleth_world(1,2021,"Mayo",2021,"Mayo")

    layout = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. ",
                style = {"margin-bottom":"0.2rem"}
                 ),],
                color="info"),
        dcc.Graph(figure = grafico, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})
    ])

    return layout

def cargar_geo_filtros(tipo=1,pais="",dpto="",pos="",cat="",mesini='Mayo',anoini=2021,mesfin='Mayo',anofin=2021):

    grafico= ugc.update_choropleth_world(tipo,"","","","",mesini,anoini,mesfin,anofin)

    layout = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. ",
                style = {"margin-bottom":"0.2rem"}
                 ),],
                color="info"),
        dcc.Graph(figure = grafico, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})
    ])

    return layout