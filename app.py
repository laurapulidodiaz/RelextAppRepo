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
from view import daniel_view as daniel
from view import mari_view as mari

GLOBAL_STYLE = {
    "font-size" : "0.8rem"
}

# cargamos el app con plantilla bootstrap
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP] , update_title='Cargando...')
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

# cargamos la plantilla
app.layout = html.Div(children=[
        dcc.Location(id="url"),
        menu.cargar_navbar(app),
        html.Div(children=[
            sidebar.cargar_sidebar(app, "Consulta de Registros","Datos Históricos"),
            content.cargar_content(),
        ],
        style= GLOBAL_STYLE
    ),
])

# definimos enrutamiento
@app.callback(Output(content.CONTENT_DIV_ID, "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == menu.CONSULTAR:
        return consultar.layout
    elif pathname == menu.VISUALIZAR:
        return visualizar.layout
    elif pathname == menu.CARGAR:
        return cargar.layout
    elif pathname == menu.DANIEL:
        return daniel.layout
    elif pathname == menu.MARI:
        return mari.layout
    elif pathname == menu.MODELOS:
        return modelos.layout
    elif pathname == menu.AYUDA:
        return ayuda.layout
    elif pathname == menu.CLAVE:
        return cambiarclave.layout
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

# actualizar página de acuerdo con los filtros
@app.callback(
    Output(content.CONTENT_DIV_ID, "children"),
    [Input('filtrar_superior', 'n_clicks')],
    state=[State(component_id='dropdown_tipo_registro', component_property='value'),
    State(component_id='dropdown_pais', component_property='value'),
    State(component_id='dropdown_departamento', component_property='value'),
    State(component_id='fecha_desde_year', component_property='value'),
    State(component_id='fecha_desde_month', component_property='value'),
    State(component_id='fecha_hasta_year', component_property='value'),
    State(component_id='fecha_hasta_month', component_property='value'),
    State(component_id='input_posicion_arancelaria', component_property='value'),
    State(component_id='input_producto_texto', component_property='value'),
    State(component_id='url', component_property='pathname')]
)
def update_contenido_desde_filtro_superior(n_clicks, tipo_registro, pais, departamento, anio_desde, mes_desde, anio_hasta, mes_hasta, posicion, categoria, pathname):
    return update_contenido_desde_filtro(tipo_registro, pais, departamento, anio_desde, mes_desde, anio_hasta, mes_hasta, posicion, categoria, pathname)

@app.callback(
    Output(content.CONTENT_DIV_ID, "children"),
    [Input('filtrar_inferior', 'n_clicks')],
    state=[State(component_id='dropdown_tipo_registro', component_property='value'),
    State(component_id='dropdown_pais', component_property='value'),
    State(component_id='dropdown_departamento', component_property='value'),
    State(component_id='fecha_desde_year', component_property='value'),
    State(component_id='fecha_desde_month', component_property='value'),
    State(component_id='fecha_hasta_year', component_property='value'),
    State(component_id='fecha_hasta_month', component_property='value'),
    State(component_id='input_posicion_arancelaria', component_property='value'),
    State(component_id='input_producto_texto', component_property='value'),
    State(component_id='url', component_property='pathname')]
)
def update_contenido_desde_filtro_inferior(n_clicks, input_value):
    return update_contenido_desde_filtro(tipo_registro, pais, departamento, anio_desde, mes_desde, anio_hasta, mes_hasta, posicion, categoria, pathname)



def update_contenido_desde_filtro(tipo_registro, pais, departamento, anio_desde, mes_desde, anio_hasta, mes_hasta, posicion, categoria, pathname) :
        if pathname == menu.CONSULTAR:
            return consultar.layout
        elif pathname == menu.VISUALIZAR:
            return visualizar.layout
        elif pathname == menu.CARGAR:
            return cargar.layout
        elif pathname == menu.DANIEL:
            return daniel.layout
        elif pathname == menu.MARI:
            return mari.layout
        elif pathname == menu.MODELOS:
            return modelos.layout
        elif pathname == menu.AYUDA:
            return ayuda.layout
        elif pathname == menu.CLAVE:
            return cambiarclave.layout
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
