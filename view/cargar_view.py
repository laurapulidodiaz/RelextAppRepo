import dash_bootstrap_components as dbc
import dash_html_components as html
from controller import carga_controller as cc

def cargar_mensaje_inicial() :
    mensaje_inicial = html.Div([
            dbc.Alert([
                        html.H4("Carga de Datos", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
                        html.P(
                            "En esta página puede realizar la verificación y carga de datos desde la web del DANE. El proceso de carga completa, cargará toda la información disponible desde el 2011. "
                            "Tome en cuenta que este proceso puede demorar incluso más de una hora, y no debe ser detenido.",
                            style = {"margin-bottom":"0.2rem"}
                        ),
                    ],
                color="info")
        ]
    )
    boton_completa = dbc.Button("Carga Completa", color="secondary", className="mr-1", id="loading-button_full", n_clicks=0)
    boton = dbc.Button("Actualizar Datos", color="primary", className="mr-1", id="loading-button", n_clicks=0)
    spinner = dbc.Spinner(children=[html.Div(id="loading-output")], size="lg", color="primary", type="border", fullscreen=False)
    spinner2 = dbc.Spinner(children=[html.Div(id="loading-output_full")], size="lg", color="primary", type="border", fullscreen=False)

    layout_inicial = html.Div( children = [
            mensaje_inicial,
            spinner,
            spinner2,
            boton_completa,
            boton
        ]
    )
    return layout_inicial

def iniciar_carga(completa) :
    if completa :
        cc.cargar_datos_2011()
    else :
        cc.cargar_datos()

    mensaje_final = html.Div([
            dbc.Alert([
                        html.H4("Carga Finalizada!", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
                        html.P(
                            "La carga de datos ha finalizado. ",
                            style = {"margin-bottom":"0.2rem"}
                        ),
                    ],
                color="success")
        ],
    )
    return mensaje_final
