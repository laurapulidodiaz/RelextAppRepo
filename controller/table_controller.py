import dash_table
import json
from controller import local_to_dataframes as ltd

def get_name_dpt(n, json_file):
    for j in json_file:
        if j['value'] == n:
            return j['label']
    return n


def get_table(tipo=1, anoini=2021, mesini='Mayo', anofin=2021, mesfin='Mayo'):

    if anoini is None:
        anoini = 2017
    if mesini is None:
        mesini = 'Enero'
    if anofin is None:
        anofin = 2021
    if mesfin is None:
        mesfin = 'Diciembre'

    dff = ltd.cargar_dataframes(anoini, mesini, anofin, mesfin)

    json_dpts = "data/CSV/departamentos.json"
    dpts = json.loads(open(json_dpts).read())
    if tipo<=3:
        df = dff[tipo - 1]



    if tipo == 1:
        df['Departamento de procedencia nombre'] = df['Departamento de procedencia'].apply(lambda x: get_name_dpt(x, dpts))


    

    init_columns = ['Código país destino', 'Fecha', 'Departamento de procedencia nombre',
     'Total valor FOB doláres de la posición', 'Descripción Arancelaria', 'SCN - Base 2015']

    
    
    return dash_table.DataTable(
        id='datatable',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
            for i in df.columns
        ],
        data=df.to_dict('records'),  # the contents of the table
        hidden_columns=[col for col in df.columns if col not in init_columns],
        export_format='xlsx',
        editable=False,              # allow editing of data inside all cells
        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        # column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        # row_selectable="multi",     # allow users to select 'multi' or 'single' rows
        row_deletable=False,       # choose if user can delete a row (True) or not (False)
        # selected_columns=[],        # ids of columns that user selects
        # selected_rows=[],           # indices of rows that user selects
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=15,                # number of rows visible per page
        style_cell={                # ensure adequate header width when text is shorter than cell's text
            'minWidth': 30, 'maxWidth': 180, 'width': 30
        },
        #style_cell_conditional=[    # align text columns to left. By default they are aligned to right
        #     {
        #         'if': {'column_id': c},
        #         'textAlign': 'left'
        #     } for c in ['country', 'iso_alpha3']
        # ],
        style_data={                # overflow cells' content into multiple lines
            'whiteSpace': 'normal',
            'height': 'auto'
        }
    )