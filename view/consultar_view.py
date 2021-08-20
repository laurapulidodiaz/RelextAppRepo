import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from controller import consulta_controller as controller
import plotly.express as px

df, year_selected, month_selected = controller.data_cundinamarca_top10_export()

if type(df) != int :
    grafico = px.bar(df, x="Total valor FOB doláres de la posición", y="Descripción Arancelaria Corta")
    componente_grafico = dcc.Graph(figure = grafico, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})
else :
    componente_grafico = html.P("No existe información de exportaciones para este período.")

layout = html.Div([
            dbc.Alert([
                        html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
                        html.P(
                            "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
                            " Si es la primera vez que ingresas al sistema quizás quieras empezar por uno de los productos populares en exportaciones en Cundinamarca.",
                            style = {"margin-bottom":"0.2rem"}
                        ),
                    ],
                color="info"),
            html.P("Top 10 productos exportados desde Cundinamarca en "+str(month_selected)+" de "+str(year_selected)+"" , style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
            html.P("Según su sumatoria de valores FOB en dólares en registros de exportación.", style={"font-weight":"normal","font-size":"13px","margin-top":"-16px"}),
            componente_grafico
        ]
    )
