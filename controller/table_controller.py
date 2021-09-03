import dash_table
from controller import local_to_dataframes as ltd

def get_table(tipo=1, anoini=2021, mesini='Mayo', anofin=2021, mesfin='Mayo'):
    dff = ltd.cargar_dataframes(anoini, mesini, anofin, mesfin)

    if tipo<=3:
        df = dff[tipo - 1]
    
    return dash_table.DataTable(
        id='datatable',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
            for i in df.columns
        ],
        data=df.to_dict('records'),  # the contents of the table
        hidden_columns=['FECH', 'Aduana', 'País destino', 'Lugar de Salida', 'Mes', 'Año', 'Razón social del exportador', 'Nit del exportador',
                        'Posición Arancelaria', 'Código de unidad comercial de medida (numérico)', 'ññññ'],
        editable=True,              # allow editing of data inside all cells
        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        row_selectable="multi",     # allow users to select 'multi' or 'single' rows
        row_deletable=True,         # choose if user can delete a row (True) or not (False)
        selected_columns=[],        # ids of columns that user selects
        selected_rows=[],           # indices of rows that user selects
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=15,                # number of rows visible per page
        style_cell={                # ensure adequate header width when text is shorter than cell's text
            'minWidth': 105, 'maxWidth': 105, 'width': 105
        },
        #style_cell_conditional=[    # align text columns to left. By default they are aligned to right
        #     {
        #         'if': {'column_id': c},
        #         'textAlign': 'left'
        #     } for c in ['country', 'iso_alpha3']
        # ],
        # style_data={                # overflow cells' content into multiple lines
        #     'whiteSpace': 'normal',
        #     'height': 'auto'
        # }
    )