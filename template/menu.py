import dash_bootstrap_components as dbc
import dash_html_components as html

CONSULTAR = "/"
VISUALIZAR = "/visualizar"
CARGAR = "/cargar"
MODELOS = "/modelos"
AYUDA = "/ayuda"
CLAVE = "/cambiarclave"
SALIR = "/salir"
DANIEL = "/geografico"
MARI = "/historico"
PAISES = "/paises"
DEPARTAMENTOS = "/departamentos"
ZONAS_FRANCAS = "/zonasfrancas"
BARPLOTS = "/barplots"
HISTOGRAMS = "/histogramas"
BALANZA = "/trade_balance"


def cargar_navbar(app):
    BAR_STYLE = {
        "height": "115px",
        "background-color": "#2c3e50",
    }

    NAVBAR_STYLE = {
        "position": "relative",
        "top": 20,
        "height": 40,
        "width": "160px",
        "background-color": "#031828",
        "border-radius": "6px",
        "margin": "4px",
        "padding-left": "16px",
        "padding-bottom": "11px",
        "font-size": "14px",
    }

    LOGO_STYLE = {
        "position": "absolute",
        "top": "5px",
        "left": "10px",
        "width": "250px",
    }

    STYLE_USUARIO = {
        "position": "relative",
        "top": "12px",
        "font-size": "18px",
        "font-weight": "600",
        "color": "#FFFFFF80",
        "padding-left": "12px",
        "padding-bottom": "0px",
        "padding-top": "8px",
    }

    STYLE_ROL = {
        "position": "relative",
        "top": "-8px",
        "font-size": "13px",
        "font-weight": "normal",
        "color": "#FFFFFF50",
        "padding-left": "12px",
        "padding-bottom": "0px",
        "padding-top": "4px",
    }

    STYLE_BTN_SALIR = {
        "position": "relative",
        "top": "-20px",
        "left": "16px",
        "width": "20%",
        "display": "inline-block",
        "filter": "brightness(0.8)"
    }

    usuario_nav = html.Div(
        children = [
            html.Div(
                children = [
                    html.P("Fulanito Pérez Ortega", style=STYLE_USUARIO),
                    html.P("Analista de Datos", style=STYLE_ROL)
                ],
                style={"width": "80%", "display": "inline-block"}
            ),
            html.Img(src=app.get_asset_url('icono_salir.png'), style=STYLE_BTN_SALIR),
        ],
        style = {"position": "relative", "left": "40px"}
    )

    navbar = dbc.NavbarSimple(
        children=[
            html.Img(src=app.get_asset_url('logo.png'), style=LOGO_STYLE),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Registros de Datos", href=CONSULTAR),
                    dbc.DropdownMenuItem("Visualización Geográfica", href=DANIEL),
                    dbc.DropdownMenuItem("Comportamiento Histórico", href=MARI),
                    dbc.DropdownMenuItem("Productos TOP", href=BARPLOTS),
                    dbc.DropdownMenuItem("Gráficos de Distribución", href=HISTOGRAMS)
                ],
                nav=True,
                in_navbar=True,
                label="Datos",
                style=NAVBAR_STYLE,
            ),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Configuración de Datos", href=ZONAS_FRANCAS),
                    dbc.DropdownMenuItem("Carga de Datos", href=CARGAR),
                ],
                nav=True,
                in_navbar=True,
                label="Administración",
                style=NAVBAR_STYLE,
            ),
            usuario_nav
        ],
        color="#2c3e50",
        dark=True,
        style=BAR_STYLE,
    )

    return navbar
