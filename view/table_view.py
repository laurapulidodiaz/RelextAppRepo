import dash_bootstrap_components as dbc
import dash_html_components as html
from controller import table_controller as tab_c

def table_layout(tipo=1, anoini=2021, mesini='Mayo', anofin=2021, mesfin='Mayo'):
    #Exportaciones en mes y año por defecto

    layout = html.Div([
        dbc.Alert([
            html.H4("Sugerencia", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
                "Si es la primera vez que ingresas al sistema quizás quieras empezar por uno de los productos populares en exportaciones en Cundinamarca.",
                style = {"margin-bottom":"0.2rem"}
                 ),],
                color="info"),
        #dcc.Graph(figure = grafico, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})
        tab_c.get_table(tipo=tipo, anoini=anoini, mesini=mesini, anofin=anofin, mesfin=mesfin)

    ])

    return layout