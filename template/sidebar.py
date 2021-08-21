import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

IMPORTACIONES = "/consultar/importaciones"
EXPORTACIONES = "/consultar/exportaciones"
BALANZA_COMERCIAL = "/consultar/balanza_comercial"
PRODUCCION = "/consultar/produccion"

def cargar_sidebar(app, pagina, copi) :
    SIDEBAR_STYLE = {
        "position": "absolute",
        "top": "115px",
        "left": 0,
        "bottom": 0,
        "width": "18rem",
        "padding": "2rem 1rem",
        "background-color": "#fff",
        "border-right": "solid 2px #88888840",
        "border-bottom": "solid 2px #88888850",
        "box-shadow": "4px 2px 2px 2px #f8f9fa",
    }

    ICONO_STYLE = {
        "padding": "18px 12px 12px 0px",
        "width": "48px",
    }

    PAGINA_STYLE = {
        "font-weight": "bold",
        "font-size": "18px",
    }

    TEXTO_STYLE = {
        "font-weight": "normal",
        "font-size": "13px",
        "margin-top": "-3px",
    }

    tipo_registro_input = dbc.FormGroup(
        [
            dbc.Label("Tipo de Registro", html_for="dropdown_tipo_registro"),
            dcc.Dropdown(
                id="dropdown_tipo_registro",
                options=[
                    {"label": "Exportaciones", "value": 1},
                    {"label": "Importaciones", "value": 2},
                    {"label": "Balanza Comercial", "value": 2},
                    {"label": "Producción", "value": 2},
                ],
            ),
        ]
    )

    sidebar = html.Div(
        [
            html.Img(src=app.get_asset_url('icono_gris.png'), style=ICONO_STYLE),
            html.H3(pagina, style=PAGINA_STYLE),
            html.H6(copi, style=TEXTO_STYLE),
            html.Hr(),
            tipo_registro_input,
            html.Hr(),
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar

def cargar_filtros_exportaciones() :
    filtros = dbc.FormGroup(
        [
            dbc.Label("Tipo de Registro"),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Exportaciones", href=EXPORTACIONES),
                    dbc.DropdownMenuItem("Importaciones", href=IMPORTACIONES),
                    dbc.DropdownMenuItem("Balanza Comercial", href=BALANZA_COMERCIAL),
                    dbc.DropdownMenuItem("Producción", href=PRODUCCION),
                ],
                nav=True,
                in_navbar=True,
                label="Sistema",
            ),
        ]
    )

    return filtros
