import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime
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
        month_selected = MONTHS[month_selected-4]
    else :
        year_selected = year_selected - 1
        month_selected = MONTHS[month_selected-4+12]

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

    input_date_picker = html.Div([
        dbc.Label("Rango de Fechas", html_for="my-date-picker-range"),
        dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=date(2016, 1, 1),
            max_date_allowed=date(year_selected, month_selected, day_selected)
            display_format='M MM-YYYY',
            start_date_placeholder_text='Fecha Desde'
            end_date_placeholder_text='Fecha Haste'
        ),
        html.Div(id='output-container-date-picker-range')
    ])

    sidebar = html.Div(
        [
            html.Img(src=app.get_asset_url('icono_gris.png'), style=ICONO_STYLE),
            html.H3(pagina, style=PAGINA_STYLE),
            html.H6(copi, style=TEXTO_STYLE),
            html.Hr(),
            tipo_registro_input,
            html.Hr(),
            input_date_picker
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar

@app.callback(dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')])
def update_output(start_date, end_date):
    string_prefix = 'You have selected: '
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%Y%m')
        string_prefix = string_prefix + 'Fecha Desde: ' + start_date_string + ' | '
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%Y%m')
        string_prefix = string_prefix + 'Fecha Hasta: ' + end_date_string
    if len(string_prefix) == len('Usted ha seleccionado: '):
        return 'La fecha se mostrará aquí'
    else:
        return string_prefix

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
