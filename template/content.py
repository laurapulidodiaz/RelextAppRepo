import dash_html_components as html

CONTENT_DIV_ID = "page-content"

def cargar_content() :

    CONTENT_STYLE = {
        "margin-left": "19rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    }

    content = html.Div(id=CONTENT_DIV_ID, style=CONTENT_STYLE)

    return content
