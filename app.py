# libs base para el desarrollo de la interfaz
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from whitenoise import WhiteNoise

# contienen funciones para cargar las partes del template
from template import menu
from template import sidebar
from template import content

# contienen funciones para cargar contenido por modulo
from view import ayuda_view as ayuda
from view import cambiar_clave_view as cambiarclave
from view import consultar_view as consultar
from view import cargar_view as cargar
from view import modelos_view as modelos
from view import visualizar_view as visualizar
from view import geographic_view as geov
from view import mari_view as mari
from view import table_view as table
from view.admin import pais_view as paisv
from view.admin import departamento_view as departamentov
from view.admin import zona_franca_view as zonafrancav
from view import juliana_view as juli

from controller import local_to_dataframes as ltd

GLOBAL_STYLE = {
    "font-size": "0.8rem"
}

# cargamos el app con plantilla bootstrap
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], update_title='Cargando...')
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

# cargamos la plantilla
app.layout = html.Div(children=[
        dcc.Location(id="url"),
        menu.cargar_navbar(app),
        html.Div(children=[
            sidebar.cargar_sidebar(app, "Consulta de Registros", "Datos Históricos"),
            content.cargar_content(),
        ],
            style=GLOBAL_STYLE
        ),
])

# definimos enrutamiento
@app.callback(
    Output(content.CONTENT_DIV_ID, "children"),
    [
        Input("url", "pathname"),
        Input('filtrar_superior', 'n_clicks'),
        Input('filtrar_inferior', 'n_clicks'),
    ],
    [
        State(component_id='dropdown_tipo_registro', component_property='value'),
        State(component_id='dropdown_pais', component_property='value'),
        State(component_id='dropdown_departamento', component_property='value'),
        State(component_id='fecha_desde_year', component_property='value'),
        State(component_id='fecha_desde_month', component_property='value'),
        State(component_id='fecha_hasta_year', component_property='value'),
        State(component_id='fecha_hasta_month', component_property='value'),
        State(component_id='input_posicion_arancelaria', component_property='value'),
        State(component_id='url', component_property='pathname')
    ]
)
def render_page_content(pathname, click1, click2, tipo_registro, pais, departamento, anio_desde, mes_desde,
                        anio_hasta, mes_hasta, posicion, pathname2):
    if pathname == menu.CONSULTAR:
        return table.table_layout()
    elif pathname == menu.VISUALIZAR:
        return visualizar.layout
    elif pathname == menu.CARGAR:
        return cargar.layout
    #elif pathname == menu.TABLE:
    #    return table.table_layout()
    elif pathname == menu.DANIEL:
        if click1 or click2:
            return geov.cargar_geo_filtros(tipo_registro, pais, departamento, posicion, "",
                                            mes_desde, anio_desde, mes_hasta, anio_hasta)
        else:
            return geov.cargar_geo()
    elif pathname == menu.MARI:
        if click1 or click2:
            return mari.cargar_mari_filtros(tipo_registro, pais, departamento, posicion,
                                            mes_desde, anio_desde, mes_hasta, anio_hasta)
        else:
            return mari.cargar_mari()
    elif pathname == menu.MODELOS:
        return modelos.layout
    elif pathname == menu.AYUDA:
        return ayuda.layout
    elif pathname == menu.CLAVE:
        return cambiarclave.layout
    elif pathname == menu.PAISES:
        return paisv.layout
    elif pathname == menu.DEPARTAMENTOS:
        return departamentov.layout
    elif pathname == menu.ZONAS_FRANCAS:
        return zonafrancav.layout
    elif pathname == menu.BARPLOTS:
        if click1 or click2:
            return juli.barplot_juli_filtros(tipo_registro,pais,departamento,posicion,categoria,
                                 mes_desde,anio_desde,mes_hasta,anio_hasta)
        else:
            return juli.barplot_juli()
    elif pathname == menu.HISTOGRAMS:
        if click1 or click2:
            return juli.histogram_juli_filtro(tipo_registro,pais,departamento,categoria,posicion,
                                         anio_desde,mes_desde,anio_hasta,mes_hasta)
        else:
            return juli.histogram_juli()
    elif pathname == menu.BALANZA:
        if click2:
            return juli.balanza_filtros(posicion, anio_desde,mes_desde, anio_hasta, mes_hasta)
        else:
            return juli.balanza_default()
    elif pathname == menu.SALIR:
        return html.P("Por implementar... cierre de sesión.")

    # En caso de una ruta inválida
    return dbc.Jumbotron(
        [
            html.H1("Oooops! Página no encontrada!", className="text-danger"),
            html.Hr(),
            html.P(f"La ruta {pathname} no se reconoce..."),
        ]
    )


# inicializamos la aplicacion en el server
if __name__ == "__main__":
    app.run_server(port=8888)
