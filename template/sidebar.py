import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime, date
from controller.local_to_dataframes import MONTHS

IMPORTACIONES = "/consultar/importaciones"
EXPORTACIONES = "/consultar/exportaciones"
BALANZA_COMERCIAL = "/consultar/balanza_comercial"
PRODUCCION = "/consultar/produccion"

def cargar_sidebar(app, pagina, copi) :
    year_selected = datetime.today().year
    month_selected = datetime.today().month
    day_selected = datetime.today().day

    if month_selected > 3 :
        month_selected = month_selected-3
    else :
        year_selected = year_selected - 1
        month_selected = month_selected-4+12

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
                    {"label": "Balanza Comercial", "value": 3},
                    {"label": "Producción", "value": 4},
                ],
            ),
        ]
    )

    def crear_year_picker(nuevo_id) :
        years = []
        for year in range ((year_selected),(year_selected-5),-1) :
            year_values = {"label": str(year), "value": year}
            years.append(year_values)

        year_picker = dcc.Dropdown(
                id=nuevo_id,
                placeholder="Año",
                options=years,
            )
        return year_picker



    def crear_month_picker(nuevo_id_month) :
        months = []
        contador = 0
        for month in MONTHS :
            contador+=1
            month_values = {"label": month, "value": contador}
            months.append(month_values)

        month_picker = dcc.Dropdown(
                id=nuevo_id_month,
                placeholder="Mes",
                options=months,
            )
        return month_picker

    input_date_picker_desde = dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Desde", html_for="fecha_desde_year"),
                        crear_year_picker("fecha_desde_year"),
                    ]
                ),
                width=6,
            ),
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("-", html_for="fecha_desde_month", style={"color":"#fff"}),
                        crear_month_picker("fecha_desde_month"),
                    ]
                ),
                width=6,
            ),
        ],
        form=True,
    )
    input_date_picker_hasta = dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("Hasta", html_for="fecha_hasta_year"),
                        crear_year_picker("fecha_haste_year"),
                    ]
                ),
                width=6,
            ),
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label("-", html_for="fecha_hasta_month", style={"color":"#fff"}),
                        crear_month_picker("fecha_hasta_month"),
                    ]
                ),
                width=6,
            ),
        ],
        form=True,
    )

    input_posicion_arancelaria = html.Div(
        [
            html.P("Posición Arancelaria (producto)"),
            dbc.Input(id="input_posicion_arancelaria", placeholder="Digite el número...", type="number"),
        ],
    )

    input_texto_descripcion = html.Div(
        [
            html.P("Producto / Categoría"),
            dbc.Input(id="input_producto_texto", placeholder="Digite el texto...", type="text"),
        ],
    )

    sidebar = html.Div(
        [
            html.Img(src=app.get_asset_url('icono_gris.png'), style=ICONO_STYLE),
            html.H3(pagina, style=PAGINA_STYLE),
            html.H6(copi, style=TEXTO_STYLE),
            html.Hr(),
            tipo_registro_input,
            html.Hr(),
            dbc.Label("Rango de Fechas"),
            input_date_picker_desde,
            input_date_picker_hasta,
            input_posicion_arancelaria,
            input_texto_descripcion,
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
