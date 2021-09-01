import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from controller import consulta_controller as controller
from controller import update_graph_controller as upc

df_exports, df_imports, data_balance = controller.loc_grouped(date_start=0, date_end=0)


if type(df_exports) != int :
    grafico = upc.update_choropleth_world(df_exports)
    componente_grafico = dcc.Graph(figure = grafico, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})
else :
    componente_grafico = html.P("No existe información de exportaciones para este período.")

layout = html.Div([
            dbc.Alert([
                        html.H4("Sugerencia", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
                        html.P(
                            "Por favor, haz tu selección en algunos filtros para obtener información particular de los registros históricos. "
                            "Por defecto, este mapa muestra las exportaciones según el país de destino en Mayo de 2021.",
                            style = {"margin-bottom":"0.2rem"}
                        ),
                    ],
                color="info"),
            html.P("Según sumatoria de valores FOB en dólares en registros de exportación.", style={"font-weight":"normal","font-size":"13px","margin-top":"-16px"}),
            componente_grafico
        ]
    )
