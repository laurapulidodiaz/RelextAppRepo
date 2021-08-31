import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc


layout = html.Div([
            dbc.Alert([
                        html.H4("Bienvenido", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
                        html.P(
                            "Esta es una herramienta de consulta, visualización y análisis de la información de exportaciones e importaciones en Colombia."
                            "La información disponible abarca desde el año 2016 hasta el periodo más reciente de la información publicada por el DANE.",
                            style = {"margin-bottom":"0.2rem"}
                        ),
                    ],
                color="info"),
            html.P("¿Cómo utilizar esta herramienta?"" , style={"font-weight":"600","font-size":"16px","margin-top":"24px"}),
            html.P(<ol>
                    <li> 'En la pestaña' <q>'Datos'</q> 'seleccione el tipo de consulta que desea visualizar.', style={"font-weight":"normal","font-size":"13px","margin-top":"-16px"}),
            componente_grafico
        ]
    )
