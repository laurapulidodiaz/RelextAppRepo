import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from controller import consulta_controller as controller
import plotly.express as px
from controller import mari_controller as mari
from controller import local_to_dataframes as ld

grafico=mari.lineplot("Exportaciones","","","","","Mayo",2021,"Mayo",2021)

layout = html.Div([
    dbc.Alert([
        html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
        html.P(
            "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
            " Si es la primera vez que ingresas al sistema quizás quieras empezar por uno de los productos populares en exportaciones en Cundinamarca.",
            style = {"margin-bottom":"0.2rem"}
             ),],
            color="info"),
    dcc.Graph(figure = grafico, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})
]),


grafico=mari.lineplot("Exportaciones","","","","","Mayo",2021,"Mayo",2021)
#mari.lineplot(tipo,pais,dpto,pos,cat,"Enero",2020,"Diciembre",2020)