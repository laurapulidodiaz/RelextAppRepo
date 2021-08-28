from controller import juliana_controller as juli
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

#grafico1 = juli.barplot_10_top(1, "USA", 25, 'dollars', "", 2021, "Mayo", 2021, "Mayo", )
#componente_grafico1 = dcc.Graph(figure = grafico1, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

def barplot_juli():
    grafico1 = juli.barplot_10_top(1,249,25,"", 2021, "Mayo", 2021, "Mayo")

    layout1 = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
                 ,style = {"margin-bottom":"0.2rem"}
            ),
        ],
            color="info"),
        html.P("Top 10 productos exportados", style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
        html.P("Según la cantidad total de unidades vendidas.", style={"font-weight":"normal","font-size":"13px","margin-top":"-16px"}),
        dcc.Graph(figure = grafico1, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

    ])


def barplot_juli_filtros(tipo_registro,pais,departamento,posicion,categoria,mes_desde,anio_desde,mes_hasta,anio_hasta):
    grafico1 = juli.barplot_10_top(tipo_registro,pais,departamento,categoria,anio_desde,mes_desde,anio_hasta,mes_hasta)

    layout1 = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
                 ,style = {"margin-bottom":"0.2rem"}
            ),
        ],
            color="info"),
        html.P("Top 10 productos exportados", style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
        html.P("Según la cantidad total de unidades vendidas.", style={"font-weight":"normal","font-size":"13px","margin-top":"-16px"}),
        dcc.Graph(figure = grafico1, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

    ])


def histogram_juli():
    grafico2 = juli.make_histogram(1, 249, 25, '', '', 2021, "Mayo", 2021, "Mayo")

    layout2 = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
                ,
                style = {"margin-bottom":"0.2rem"}
            ),
        ],
            color="info"),
        html.P("Histograma de distribución de las cantidades comercializadas", style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
        dcc.Graph(figure = grafico2, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})


])

def histogram_juli_filtro(tipo_registro,pais,departamento,categoria,posicion,anio_desde,mes_desde,anio_hasta,mes_hasta):
    grafico2=juli.make_histogram(tipo_registro,pais,departamento,categoria,posicion,anio_desde,mes_desde,anio_hasta,mes_hasta)

    layout2 = html.Div([
        dbc.Alert([
            html.H4("Iniciar", className="alert-heading",
                    style={"font-size": "20px", "padding-top": "8px", "font-weight": "400"}),
            html.P(
                "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
                ,
                style={"margin-bottom": "0.2rem"}
            ),
        ],
            color="info"),
        html.P("Histograma de distribución de las cantidades comercializadas",
               style={"font-weight": "600", "font-size": "16px", "margin-top": "24px"}),
        dcc.Graph(figure=grafico2,
                  style={"font-weight": "normal", "font-size": "13px", "margin-left": "24px", "margin-top": "-18px"})

    ])