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

    def cargar_paises() :
        paises = [{"value":1,"label":"ZFPE Agroindustrial"},{"value":2,"label":"ZFP El Dorado"},{"value":3,"label":"ZFECA Ecopetrol"},{"value":4,"label":"ZF CTIC-Centro"},{"value":13,"label":"Afganistán"},{"value":15,"label":"Islas Aland"},{"value":17,"label":"Albania"},{"value":23,"label":"Alemania"},{"value":24,"label":"Antartida"},{"value":26,"label":"Armenia"},{"value":27,"label":"Aruba"},{"value":29,"label":"Bosnia-Herzegovina"},{"value":31,"label":"Burkina Fasso"},{"value":37,"label":"Andorra"},{"value":40,"label":"Angola"},{"value":41,"label":"Anguilla"},{"value":43,"label":"Antigua y Barbuda"},{"value":47,"label":"Antillas Holandesas"},{"value":53,"label":"Arabia Saudita"},{"value":59,"label":"Argelia"},{"value":63,"label":"Argentina"},{"value":69,"label":"Australia"},{"value":72,"label":"Austria"},{"value":74,"label":"Azerbaijan"},{"value":77,"label":"Bahamas"},{"value":80,"label":"Bahrein"},{"value":81,"label":"Bangladesh"},{"value":83,"label":"Barbados"},{"value":87,"label":"Bélgica"},{"value":88,"label":"Belice"},{"value":90,"label":"Bermudas"},{"value":91,"label":"Belarus"},{"value":93,"label":"Birmania (Myanmar)"},{"value":97,"label":"Bolivia"},{"value":98,"label":"San Eus Bonaire"},{"value":101,"label":"Botswana"},{"value":102,"label":"Isla Bouvet"},{"value":105,"label":"Brasil"},{"value":108,"label":"Brunei Darussalam"},{"value":111,"label":"Bulgaria"},{"value":115,"label":"Burundi"},{"value":119,"label":"Bután"},{"value":127,"label":"Cabo Verde"},{"value":129,"label":"ZFP Zofrandina"},{"value":130,"label":"ZFPE Colmotores"},{"value":131,"label":"ZFPE Tablemac MDF"},{"value":132,"label":"ZFPE Fundación Cardiovascular"},{"value":133,"label":"ZFPE Aceites cimarrones"},{"value":134,"label":"ZFPE Puerto Brisa"},{"value":135,"label":"ZFPE Clínica Cardiovascular Corazón Joven"},{"value":137,"label":"Islas Caimán"},{"value":141,"label":"Camboya (Kampuchea)"},{"value":145,"label":"República Unida del Camerún"},{"value":149,"label":"Canadá"},{"value":155,"label":"Islas Anglonormandas"},{"value":156,"label":"Ceilán"},{"value":157,"label":"Islas Cantón y Enderburry"},{"value":159,"label":"Santa Sede"},{"value":165,"label":"Islas Cocos (Keeling)"},{"value":169,"label":"Colombia"},{"value":173,"label":"Comoras"},{"value":177,"label":"Congo"},{"value":183,"label":"Islas Cook"},{"value":187,"label":"República Popular Democrática de Corea (Norte)"},{"value":190,"label":"República de Corea (Sur)"},{"value":193,"label":"Costa de Marfil"},{"value":196,"label":"Costa Rica"},{"value":198,"label":"Croacia"},{"value":199,"label":"Cuba"},{"value":200,"label":"Curazao"},{"value":203,"label":"Chad"},{"value":211,"label":"Chile"},{"value":215,"label":"China"},{"value":218,"label":"Taiwan (Formosa)"},{"value":221,"label":"Chipre"},{"value":229,"label":"Benin"},{"value":232,"label":"Dinamarca"},{"value":235,"label":"Dominica"},{"value":239,"label":"Ecuador"},{"value":240,"label":"Egipto"},{"value":242,"label":"El Salvador"},{"value":243,"label":"Eritrea"},{"value":244,"label":"Emiratos Árabes Unidos"},{"value":245,"label":"España"},{"value":246,"label":"Eslovaquia"},{"value":247,"label":"Eslovenia"},{"value":249,"label":"Estados Unidos"},{"value":251,"label":"Estonia"},{"value":253,"label":"Etiopia"},{"value":259,"label":"Islas Feroe"},{"value":267,"label":"Filipinas"},{"value":271,"label":"Finlandia"},{"value":275,"label":"Francia"},{"value":281,"label":"Gabón"},{"value":285,"label":"Gambia"},{"value":287,"label":"Georgia"},{"value":289,"label":"Ghana"},{"value":293,"label":"Gibraltar"},{"value":297,"label":"Granada"},{"value":301,"label":"Grecia"},{"value":305,"label":"Groenlandia"},{"value":309,"label":"Guadalupe"},{"value":313,"label":"Guam"},{"value":317,"label":"Guatemala"},{"value":325,"label":"Guayana Francesa"},{"value":327,"label":"Guernsey"},{"value":329,"label":"Guinea"},{"value":331,"label":"Guinea Ecuatorial"},{"value":334,"label":"Guinea-Bissau"},{"value":337,"label":"Guyana"},{"value":341,"label":"Haití"},{"value":343,"label":"Heard y Mc Dona"},{"value":345,"label":"Honduras"},{"value":351,"label":"Hong Kong"},{"value":355,"label":"Hungría"},{"value":361,"label":"India"},{"value":365,"label":"Indonesia"},{"value":369,"label":"Irak"},{"value":372,"label":"República Islámica del Irán"},{"value":375,"label":"Irlanda (Eire)"},{"value":379,"label":"Islandia"},{"value":383,"label":"Israel"},{"value":386,"label":"Italia"},{"value":391,"label":"Jamaica"},{"value":395,"label":"Islas Johnston"},{"value":399,"label":"Japón"},{"value":401,"label":"Jersey"},{"value":403,"label":"Jordania"},{"value":406,"label":"Kazajstán"},{"value":410,"label":"Kenia"},{"value":411,"label":"Kiribati"},{"value":412,"label":"Kirguizistán"},{"value":413,"label":"Kuwait"},{"value":420,"label":"República Popular Democrática de Laos"},{"value":426,"label":"Lesotho"},{"value":429,"label":"Letonia"},{"value":431,"label":"Líbano"},{"value":434,"label":"Liberia"},{"value":438,"label":"Libia (Incluye Fezzan)"},{"value":440,"label":"Liechtenstein"},{"value":443,"label":"Lituania"},{"value":445,"label":"Luxemburgo"},{"value":447,"label":"Macao"},{"value":448,"label":"Macedonia"},{"value":450,"label":"Madagascar"},{"value":455,"label":"Malaysia"},{"value":458,"label":"Malawi"},{"value":461,"label":"Maldivas"},{"value":464,"label":"Mali"},{"value":467,"label":"Malta"},{"value":468,"label":"Isla de Man"},{"value":469,"label":"Islas Marianas del Norte"},{"value":472,"label":"Islas Marshall"},{"value":474,"label":"Marruecos"},{"value":477,"label":"Martinica"},{"value":485,"label":"Mauricio"},{"value":488,"label":"Mauritania"},{"value":489,"label":"Mayote"},{"value":493,"label":"México"},{"value":494,"label":"Estados Federados de Micronesia"},{"value":495,"label":"Islas Midway"},{"value":496,"label":"Moldavia"},{"value":497,"label":"Mongolia"},{"value":498,"label":"Mónaco"},{"value":500,"label":"Montenegro"},{"value":501,"label":"Isla Monserrat"},{"value":505,"label":"Mozambique"},{"value":507,"label":"Namibia"},{"value":508,"label":"Nauru"},{"value":511,"label":"Islas Navidad (Christmas)"},{"value":517,"label":"Nepal"},{"value":521,"label":"Nicaragua"},{"value":525,"label":"Níger"},{"value":528,"label":"Nigeria"},{"value":531,"label":"Isla Niue"},{"value":535,"label":"Isla Norfolk"},{"value":538,"label":"Noruega"},{"value":542,"label":"Nueva Caledonia"},{"value":545,"label":"Papuasia Nueva Guinea"},{"value":548,"label":"Nueva Zelandia"},{"value":551,"label":"Vanuatu"},{"value":556,"label":"Omán"},{"value":563,"label":"Islas Pacifico (Usa)"},{"value":566,"label":"Islas Ultramarinas Menores de los Estados Unidos"},{"value":573,"label":"Países Bajos (Holanda)"},{"value":576,"label":"Pakistán"},{"value":578,"label":"Islas Palau"},{"value":579,"label":"Territorios autónomos de Palestina"},{"value":580,"label":"Panamá"},{"value":586,"label":"Paraguay"},{"value":587,"label":"Península de Malasia"},{"value":589,"label":"Perú"},{"value":593,"label":"Isla Pitcairn"},{"value":599,"label":"Polinesia Francesa"},{"value":603,"label":"Polonia"},{"value":607,"label":"Portugal"},{"value":611,"label":"Puerto Rico"},{"value":618,"label":"Qatar"},{"value":620,"label":"ZFE Sociedad Puerto Industrial Aguadulce S.A."},{"value":621,"label":"ZF Internacional del Valle"},{"value":622,"label":"ZFPE FRESENIUS MEDICAL CARE Servicio RENAL"},{"value":623,"label":"ZFP Destilería Riopaila"},{"value":624,"label":"ZFPE Puerto Bahía"},{"value":625,"label":"ZFPE Medical DUARTE"},{"value":626,"label":"ZFPE Sociedad Portuaria Regional de Buenaventura"},{"value":628,"label":"Reino Unido"},{"value":630,"label":"ZFP Barranquilla Internacional Terminal company"},{"value":631,"label":"ZFP Palermo"},{"value":632,"label":"ZFP Santelka Enterprise"},{"value":633,"label":"ZFP FEMSA"},{"value":634,"label":"ZFPE SYKES"},{"value":635,"label":"ZFPE Sociedad Portuaria Puerto Nuevo"},{"value":636,"label":"ZFPE Termotasajero"},{"value":637,"label":"ZFPE Sociedad P 637"},{"value":638,"label":"ZFPE GETCOM"},{"value":640,"label":"República Centroafricana"},{"value":644,"label":"República Checa"},{"value":647,"label":"República Dominicana"},{"value":650,"label":"Zona Franca Permanente Especial Centro Hospitalario Serena del Mar"},{"value":651,"label":"ZF Puerto Mamonal"},{"value":652,"label":"ZF Promotora Industrial y Logística de Ibagué S.A.S"},{"value":653,"label":"ZF Aceites y Grasas de Catatumbo"},{"value":655,"label":"ZFPE Plaza Mayo"},{"value":656,"label":"ZFPE Clínica de"},{"value":657,"label":"ZFPE Clínica Un"},{"value":660,"label":"Reunión"},{"value":665,"label":"Zimbabue"},{"value":670,"label":"Rumania"},{"value":675,"label":"Ruanda"},{"value":676,"label":"Rusia"},{"value":677,"label":"Islas Salomón"},{"value":685,"label":"Sahara Occidental"},{"value":687,"label":"Samoa"},{"value":688,"label":"Serbia y Montenegro"},{"value":690,"label":"Samoa Norteamericana"},{"value":693,"label":"San Bartolome"},{"value":695,"label":"San Cristóbal y Nieves"},{"value":697,"label":"San Marino"},{"value":698,"label":"San Martin (Parte Francesa)"},{"value":699,"label":"San Martin (Parte Holandesa)"},{"value":700,"label":"San Pedro y Miguelón"},{"value":705,"label":"San Vicente y Las Granadinas"},{"value":710,"label":"Santa Elena"},{"value":715,"label":"Santa Lucia"},{"value":720,"label":"Santo Tome y Príncipe"},{"value":728,"label":"Senegal"},{"value":729,"label":"Serbia"},{"value":731,"label":"Seychelles"},{"value":735,"label":"Sierra Leona"},{"value":741,"label":"Singapur"},{"value":744,"label":"República Árabe de Siria"},{"value":748,"label":"Somalia"},{"value":750,"label":"Sri Lanka"},{"value":756,"label":"República de Sudáfrica"},{"value":759,"label":"Sudan"},{"value":760,"label":"Sudan del Sur"},{"value":764,"label":"Suecia"},{"value":767,"label":"Suiza"},{"value":770,"label":"Surinam"},{"value":772,"label":"Islas Svalbard y Jan Mayen"},{"value":773,"label":"Swazilandia"},{"value":774,"label":"Tadjikistán"},{"value":776,"label":"Tailandia"},{"value":780,"label":"República Unida de Tanzania"},{"value":783,"label":"Djibouti"},{"value":786,"label":"Territorios Franceses del Sur"},{"value":787,"label":"Territorio Británico del Océano Indico"},{"value":788,"label":"Timor del Este"},{"value":791,"label":"ZFPE Sociedad P"},{"value":792,"label":"ZFP Repsol Expl"},{"value":794,"label":"ZFPE Empresa Co"},{"value":795,"label":"ZFPE Onelink Co"},{"value":796,"label":"ZFPCA Petrobras"},{"value":797,"label":"ZFPE Impala Ter"},{"value":800,"label":"Togo"},{"value":805,"label":"Tokelau"},{"value":810,"label":"Tonga"},{"value":815,"label":"Trinidad y Tobago"},{"value":820,"label":"Túnez"},{"value":823,"label":"Islas Turcas y Caicos"},{"value":825,"label":"Turkmenistán"},{"value":827,"label":"Turquía"},{"value":828,"label":"Tuvalu"},{"value":830,"label":"Ucrania"},{"value":833,"label":"Uganda"},{"value":845,"label":"Uruguay"},{"value":847,"label":"Uzbekistán"},{"value":850,"label":"Venezuela"},{"value":855,"label":"Vietnam"},{"value":863,"label":"Islas Vírgenes(Británicas)"},{"value":866,"label":"Islas Vírgenes (Norteamericanas)"},{"value":870,"label":"Fiji"},{"value":873,"label":"Islas Wake"},{"value":875,"label":"Islas Wallis y Fortuna"},{"value":880,"label":"Yemen"},{"value":885,"label":"Yugoslavia"},{"value":888,"label":"Zaire"},{"value":890,"label":"Zambia"},{"value":897,"label":"Zona Neutral Palestina"},{"value":900,"label":"ZFP Andina"},{"value":902,"label":"ZFPE Gecelca3"},{"value":903,"label":"ZFPE Cementera del Magdalena Medio"},{"value":904,"label":"ZFPE Extractora la Gloria"},{"value":905,"label":"ZPFE Olmue"},{"value":907,"label":"ZFP Centro Logístico del Pacífico CELPA"},{"value":911,"label":"ZFP Barranquilla"},{"value":912,"label":"ZFP Buenaventura"},{"value":913,"label":"ZFP Palmaseca - Cali"},{"value":914,"label":"ZFP Cúcuta"},{"value":915,"label":"ZFP Santa Marta"},{"value":916,"label":"ZFP Cartagena"},{"value":917,"label":"ZFP Rionegro - Medellín"},{"value":918,"label":"ZFP Candelaria - Cartagena"},{"value":919,"label":"ZF de Bogotá"},{"value":920,"label":"ZF de Pacifico - Cali"},{"value":921,"label":"ZF de Barú Beach Resort"},{"value":922,"label":"ZF de Pozos Colorados"},{"value":923,"label":"ZF de Euro Caribe de Indias"},{"value":924,"label":"ZF del Eje Cafetero"},{"value":925,"label":"ZFPE Cerveceria del Valle"},{"value":926,"label":"ZFP Agroindustrial Magdalena Medio"},{"value":927,"label":"ZFP de Bienes y Servicios Ciudadela Salud"},{"value":928,"label":"ZFP La Cayena"},{"value":929,"label":"ZFP Internacional del Atlántico"},{"value":930,"label":"ZFPE BIO D Facatativa"},{"value":931,"label":"ZFPE Biocombustible Sostenibles del Caribe"},{"value":932,"label":"ZFPE Maquilagro"},{"value":933,"label":"ZFPE Agroindustrias del Cauca"},{"value":934,"label":"ZFP Parque Industrial Dexton"},{"value":935,"label":"ZFPE Argos S.A"},{"value":936,"label":"ZFPE Gyplac S.A"},{"value":937,"label":"ZFPE KC Antioquia G.L"},{"value":938,"label":"ZFP Plic"},{"value":939,"label":"ZFP Intexzona"},{"value":940,"label":"ZFP Tayrona S.A."},{"value":941,"label":"ZFP de Urabá"},{"value":942,"label":"ZFPE Corferias"},{"value":943,"label":"ZFP Las América"},{"value":944,"label":"ZFPE Ecodiesel"},{"value":945,"label":"ZFPE Contac Center Estrategia"},{"value":946,"label":"ZFPE Paul Calley"},{"value":947,"label":"ZFPE Siemens"},{"value":948,"label":"ZFPE Pepsico"},{"value":949,"label":"ZFPE Acerías Paz del Río"},{"value":950,"label":"ZFPE de Servicios de Marinilla"},{"value":951,"label":"ZFPE Vidrio Andino"},{"value":953,"label":"ZFPE Refineria de Cartagena"},{"value":954,"label":"ZFP de Occidente"},{"value":955,"label":"ZFPE Sociedad Portuaria de Santa Marta"},{"value":956,"label":"ZFPE de Servicios Terminal de Contenedores De Cartagena \"CONTECAR"},{"value":957,"label":"ZFPE Colombina del Cauca"},{"value":958,"label":"ZFPE Termoflores"},{"value":959,"label":"ZFPE Papelfibra"},{"value":960,"label":"ZFP de Tocancipa"},{"value":961,"label":"ZFPE Telemark Spain"},{"value":962,"label":"ZFPE San Vicente de Paul"},{"value":963,"label":"ZFPE Ceramicas San Lorenzo"},{"value":964,"label":"ZFPE Papeles del Cauca"},{"value":965,"label":"ZFPE Clinica Portoazul"},{"value":966,"label":"ZFP Santander"},{"value":967,"label":"ZFPE Protisa"},{"value":968,"label":"ZFPE Praxair Gases industriales"},{"value":969,"label":"ZFPE Cencauca"},{"value":970,"label":"ZFPE Paspenta"},{"value":971,"label":"ZFPE Renovables"},{"value":972,"label":"ZFPE Econtac"},{"value":973,"label":"ZFPE Clinica Nogales"},{"value":974,"label":"ZFP Metropolitana"},{"value":975,"label":"ZFPE Agrosolera"},{"value":976,"label":"ZFPE Bioenergy"},{"value":977,"label":"ZFP Puerta de Las Americas"},{"value":978,"label":"ZFPE Sociedad Medica de Sabaneta"},{"value":979,"label":"ZFPE Productos Familia Cajica"},{"value":980,"label":"ZFPE Sociedad Portuaria de Barranquilla"},{"value":981,"label":"ZFPE Fosunab"},{"value":982,"label":"ZFPE Alimentos Nariño"},{"value":983,"label":"ZFPE Convergys"},{"value":984,"label":"ZFPE Procesadora de Aceite Ororojo"},{"value":985,"label":"ZFP Internacional de Pereira"},{"value":986,"label":"ZFPE Clinica Megacentro Pinares"},{"value":987,"label":"ZFP Brisa"},{"value":988,"label":"ZFPE Extractora Loma Fresca"},{"value":989,"label":"ZFP Parque Central"},{"value":990,"label":"ZFPE Agroindustrias Biocafe"},{"value":991,"label":"ZFP Conjunto Industrial Parque Sur"},{"value":992,"label":"ZFPE de Servicios Celta"},{"value":993,"label":"ZFPE Habla Call Center"},{"value":994,"label":"ZFP GEA"},{"value":996,"label":"ZFPE Compañía Operadora Clinica Hispanoamericana"},{"value":997,"label":"ZFP SurColombiana"},{"value":998,"label":"ZFPE Sociedad Portuaria Regional de Cartagena"},{"value":999,"label":"No Declarados"}]

        return paises

    def cargar_departamentos() :
        departamentos = [{"value":1,"label":"Petróleo Y Derivado"},{"value":5,"label":"Antioquia"},{"value":8,"label":"Atlántico"},{"value":11,"label":"Santafé De Bogotá"},{"value":13,"label":"Bolívar"},{"value":15,"label":"Boyacá"},{"value":17,"label":"Caldas"},{"value":18,"label":"Caquetá"},{"value":19,"label":"Cauca"},{"value":20,"label":"Cesar"},{"value":23,"label":"Córdoba"},{"value":25,"label":"Cundinamarca"},{"value":27,"label":"Choco"},{"value":41,"label":"Huila"},{"value":44,"label":"Guajira"},{"value":47,"label":"Magdalena"},{"value":50,"label":"Meta"},{"value":52,"label":"Nariño"},{"value":54,"label":"Norte De Santander"},{"value":63,"label":"Quindío"},{"value":66,"label":"Risaralda"},{"value":68,"label":"Santander"},{"value":70,"label":"Sucre"},{"value":73,"label":"Tolima"},{"value":76,"label":"Valle Del Cauca"},{"value":81,"label":"Arauca"},{"value":85,"label":"Casanare"},{"value":86,"label":"Putumayo"},{"value":88,"label":"San Andrés"},{"value":91,"label":"Amazonas"},{"value":94,"label":"Guainía"},{"value":95,"label":"Guaviare"},{"value":97,"label":"Vaupés"},{"value":99,"label":"Vichada"}]
        return departamentos

    input_pais = dbc.FormGroup(
        [
            dbc.Label("País", html_for="dropdown_pais"),
            dcc.Dropdown(
                id="dropdown_pais",
                options=cargar_paises(),
            ),
        ],
        style = {"padding-top":"40px"}
    )

    input_departamento = dbc.FormGroup(
        [
            dbc.Label("Departamento", html_for="dropdown_departamento"),
            dcc.Dropdown(
                id="dropdown_departamento",
                options=cargar_departamentos(),
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

    input_posicion_arancelaria = dbc.FormGroup(
        [
            html.P("Posición Arancelaria (producto)"),
            dbc.Input(id="input_posicion_arancelaria", placeholder="Digite el número...", type="number", style={"font-size":"13px"}),
        ],
    )

    input_texto_descripcion =  dbc.FormGroup(
        [
            html.P("Producto / Categoría"),
            dbc.Input(id="input_producto_texto", placeholder="Digite el texto...", type="text", style={"font-size":"13px"}),
        ],
    )

    boton_filtrar_s = html.Div([
        dbc.Button("Filtrar", id="filtrar_superior", color="info", className="mr-1", style={"right":"0", "float":"right"})
    ])

    boton_filtrar_i = html.Div([
        dbc.Button("Filtrar", id="filtrar_inferior", color="info", className="mr-1", style={"right":"0", "float":"right"})
    ])

    sidebar = html.Div([
            html.Img(src=app.get_asset_url('icono_gris.png'), style=ICONO_STYLE),
            html.H3(pagina, style=PAGINA_STYLE),
            html.H6(copi, style=TEXTO_STYLE),
            html.Hr(),
            tipo_registro_input,
            html.Hr(),
            boton_filtrar_s,
            input_pais,
            input_departamento,
            dbc.Label("Rango de Fechas"),
            input_date_picker_desde,
            input_date_picker_hasta,
            input_posicion_arancelaria,
            input_texto_descripcion,
            boton_filtrar_i,
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar
