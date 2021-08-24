from controller import juliana_controller as juli
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

grafico1 = juli.barplot_10_top(1, "USA", 25, 'dollars', "", 2021, "Mayo", 2021, "Mayo", )
componente_grafico1 = dcc.Graph(figure = grafico1, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

layout1 = html.Div([
    dbc.Alert([
        html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
        html.P(
            "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
            " Si es la primera vez que ingresas al sistema quizás quieras empezar por uno de los productos populares en exportaciones en Cundinamarca.",
            style = {"margin-bottom":"0.2rem"}
        ),
    ],
        color="info"),
    html.P("Top 10 productos exportados", style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
    html.P("Según la cantidad total de unidades vendidas.", style={"font-weight":"normal","font-size":"13px","margin-top":"-16px"}),
    componente_grafico1
])

grafico2 = juli.make_histogram(1, "USA", 25, '', '', 2021, "Mayo", 2021, "Mayo")
componente_grafico2 = dcc.Graph(figure = grafico2, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

layout2 = html.Div([
    dbc.Alert([
        html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
        html.P(
            "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
            " Si es la primera vez que ingresas al sistema quizás quieras empezar por uno de los productos populares en exportaciones en Cundinamarca.",
            style = {"margin-bottom":"0.2rem"}
        ),
    ],
        color="info"),
    html.P("Histograma de distribución de las cantidades comercializadas", style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),

    componente_grafico2
])