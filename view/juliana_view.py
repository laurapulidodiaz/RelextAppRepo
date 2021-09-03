from controller import juliana_controller as juli
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

'''
This script defines the layouts that should be call when entering in the tabs: 
'Productos TOP' and 'Gráficos de Distribución'
'''

# Defining the default plot
def barplot_juli():
    grafico1 = juli.barplot_10_top(1,249,25, 2021, "Mayo", 2021, "Mayo")

    layout1 = html.Div([
        dbc.Alert([
            html.H4("Sugerencia", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Haz tu selección en algunos filtros para obtener información particular de los registros históricos. "
                "Por defecto esta gráfica muestra los 10 productos más exportados desde Cundinamarca hacia Estados Unidos en Mayo de 2021."
                 ,style = {"margin-bottom":"0.2rem"}
            ),
        ],
            color="info"),
        html.P("Top 10 productos exportados", style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
        html.P("Según el valor total de las exportaciones.", style={"font-weight":"normal","font-size":"13px","margin-top":"-16px"}),
        dcc.Graph(figure = grafico1, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

    ])
    return layout1

# Defining the plot when user use the dropdowns
def barplot_juli_filtros(tipo_registro,pais,departamento,mes_desde,anio_desde,mes_hasta,anio_hasta):
    grafico1 = juli.barplot_10_top(tipo_registro,pais,departamento, mes_desde, anio_desde,mes_hasta,anio_hasta)

    layout1 = html.Div([
        html.P("Top 10 productos exportados", style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
        html.P("Según el valor total de las exportaciones.", style={"font-weight":"normal","font-size":"13px","margin-top":"-16px"}),
        dcc.Graph(figure = grafico1, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

    ])
    return layout1

# Defining the default plot
def histogram_juli():
    grafico2 = juli.make_histogram(1, 249, 25, '', 2021, "Mayo", 2021, "Mayo")

    layout2 = html.Div([
        dbc.Alert([
            html.H4("Sugerencia", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
            html.P(
                "Haz tu selección en algunos filtros para obtener información de registros históricos. "
                "Por defecto este gráfico muestra la distribución del valor de las exportaciones procedentes de Cundinamarca hacia Estados Unidos en Mayo de 2021."
                ,
                style = {"margin-bottom":"0.2rem"}
            ),
        ],
            color="info"),
        html.P("Histograma de distribución del valor de los negocios", style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
        html.P("Logaritmo del valor en dólares.", style={"font-weight": "normal", "font-size": "13px", "margin-top": "-16px"}),
        dcc.Graph(figure = grafico2, style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})


])
    return layout2

# Defining the plot when user use the dropdowns
def histogram_juli_filtro(tipo_registro,pais,departamento,posicion,anio_desde,mes_desde,anio_hasta,mes_hasta):
    grafico2=juli.make_histogram(tipo_registro,pais,departamento,posicion,anio_desde,mes_desde,anio_hasta,mes_hasta)

    layout2 = html.Div([
        html.P("Histograma de distribución de las cantidades comercializadas",
               style={"font-weight": "600", "font-size": "16px", "margin-top": "24px"}),
        html.P("Logaritmo del valor en dólares.",
               style={"font-weight": "normal", "font-size": "13px", "margin-top": "-16px"}),
        dcc.Graph(figure=grafico2,
                  style={"font-weight":"normal","font-size":"13px","margin-left":"24px","margin-top":"-18px"})

    ])
    return layout2