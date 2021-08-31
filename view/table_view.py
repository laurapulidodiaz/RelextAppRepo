import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from controller import table_controller as tab_c

def table_layout():
    #Exportaciones en mes y año por defecto

    layout = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. ",
                style = {"margin-bottom":"0.2rem"}
                 ),],
                color="info"),
        #dcc.Graph(figure = grafico, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})
        tab_c.get_table()

    ])

    return layout