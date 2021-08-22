import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from controller import consulta_controller as controller
import plotly.express as px
from controller import mari_controller as mari
from controller import local_to_dataframes as ld

df_exports, df_imports, df_exports_cundinamarca, df_imports_cundinamarca = ld.cargar_dataframes(2021,"Mayo",2021,"Mayo")
MONTHS = ["Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio","Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
years=[2021,2020,2019,2018,2017]

layout = html.Div([
    dbc.Alert([
        html.H4("Iniciar", className="alert-heading", style={"font-size":"20px","padding-top":"8px", "font-weight":"400"}),
        html.P(
            "Por favor, haz tu selección en algunos filtros para obtener información de registros históricos. "
            " Si es la primera vez que ingresas al sistema quizás quieras empezar por uno de los productos populares en exportaciones en Cundinamarca.",
            style = {"margin-bottom":"0.2rem"}
             ),],
            color="info"),
    html.Label(["Tipo",dcc.Dropdown(id='Tipo-dropdown', clearable=False, value="Exportaciones",
            options=[{'label': "Exportaciones", 'value': "Exportaciones"},
                {'label': "Importaciones", 'value': "Importaciones"}]),
    html.Label(["País destino o procedencia", dcc.Dropdown(id="Pais-dropdown",clearable=True,
                searchable=True, value="",options=[{'label': c, 'value': c}
                for c in df_exports['Código país destino'].drop_duplicates().sort_values().values]), #Cambiar por diccionario actualizado
    html.Label(["Departamento destino o procedencia", dcc.Dropdown(id="Dpto-dropdown",clearable=True,
                searchable=True, value="",options=[{'label': c, 'value': c}
                for c in df_exports['Departamento de procedencia'].drop_duplicates().values]),#Cambiar a dict
    html.Label(["Posición arancelaria", dcc.Dropdown(id="Pos-dropdown",clearable=True,
                searchable=True, value="",options=[{'label': c, 'value': c}
                for c in df_exports['Descripción Arancelaria'].drop_duplicates().sort_values().values]),
    html.Label(["SCN - BASE 2015", dcc.Dropdown(id="Cat-dropdown",clearable=True,
                searchable=True, value="",options=[{'label': c, 'value': c}
                for c in df_exports['Descriptiva - SCN - NUEVA BASE 2015'].drop_duplicates().sort_values().values]),
    html.Label(["Mes inicial", dcc.Dropdown(id="Mesini-dropdown",clearable=True,
                searchable=True, value="",options=[{'label': c, 'value': c} for c in MONTHS]),
    html.Label(["Año inicial", dcc.Dropdown(id="Anoini-dropdown",clearable=True,
                searchable=True, value="",options=[{'label': c, 'value': c} for c in years]),
    html.Label(["Mes final", dcc.Dropdown(id="Mesfin-dropdown",clearable=True,
                searchable=True, value="",options=[{'label': c, 'value': c} for c in MONTHS]),
    html.Label(["Año final", dcc.Dropdown(id="Anofin-dropdown",clearable=True,
                searchable=True, value="",options=[{'label': c, 'value': c} for c in years]),
    ])
    ])
    ])
    ])
    ])
    ])
    ])
    ])
    ]),
])
# Define callback to update graph
#callback(
    #Output('graph', 'figure'),
    #Input("Tipo-dropdown", "value"),
    #Input("Pais-dropdown","value"),
    #Input("Dpto-dropdown","value"),
    #Input("Pos-dropdown","value"),
    #Input("Cat-dropdown","value"),
    #Input('Mesini-dropdown', 'value'),
    #Input('Anoini-dropdown', 'value'),
    #Input('Mesfin-dropdown', 'value'),
    #Input('Anofin-dropdown', 'value')
#)

mari.lineplot("Exportaciones","","","","","Mayo",2021,"Mayo",2021)
#mari.lineplot(tipo,pais,dpto,pos,cat,"Enero",2020,"Diciembre",2020)