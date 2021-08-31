import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from controller import consulta_controller as controller
import plotly.express as px
from controller import mari_controller as mari
from controller import local_to_dataframes as ld

def cargar_mari():
    grafico=mari.lineplot(1,"Mayo",2021,"Mayo",2021,"","","")

    layout = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. ",
                style = {"margin-bottom":"0.2rem"}
                 ),],
                color="info"),
        html.P("Comportamiento histórico ", style={"font-weight": "600", "font-size": "16px", "margin-top": "24px"}),
        html.P("Según su sumatoria de valores FOB en dólares.",style={"font-weight": "normal", "font-size": "13px", "margin-top": "-16px"}),
        dcc.Graph(figure = grafico, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

    ])
    return layout

def cargar_mari_filtros(tipo,pais,dpto,pos,mesini,anoini,mesfin,anofin):
    print("pruebaaaa 1111", mesini,anoini,mesfin,anofin)
    grafico = mari.lineplot(tipo,mesini,anoini,mesfin,anofin,pais,dpto,pos)


    layout = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading",
                    style={"font-size": "20px", "padding-top": "8px", "font-weight": "400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. ",
                style={"margin-bottom": "0.2rem"}
            ), ],
            color="info"),
        html.P("Comportamiento histórico ", style={"font-weight": "600", "font-size": "16px", "margin-top": "24px"}),
        html.P("Según su sumatoria de valores FOB en dólares.",
               style={"font-weight": "normal", "font-size": "13px", "margin-top": "-16px"}),
        dcc.Graph(figure=grafico,
                  style={"font-weight": "normal", "font-size": "13px", "margin-left": "24px", "margin-top": "-18px"})
    ])

    return layout


#mari.lineplot(tipo,pais,dpto,pos,cat,"Enero",2020,"Diciembre",2020)
