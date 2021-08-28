from controller import local_to_dataframes as ltd
import plotly.express as px

def barplot_10_top(data, country, department, category, year_start, month_start, year_end, month_end):
    if country == None:
        country = 11
    if department == None:
        department = 25
    if category == None:
        category = ""
    if year_start == None:
        year_start = 2021
    if month_start == None:
        month_start = "Mayo"
    if year_end == None:
        year_end = 2021
    if month_end == None:
        month_end = "Mayo"

    print("pruebaaa Juli", country, department)
    POS = ""
    df_exports, df_imports = ltd.dataframes_all_filtros(year_start, month_start, year_end, month_end, country,
                                                        department, POS, category)
    print(df_exports.head(2))
    # For dataset of exports
    if data == 1:
        # Adjusting character values
        df_exports['Descripción Arancelaria'] = df_exports['Descripción Arancelaria'].astype(str)
        df_exports['Descripción Arancelaria Corta'] = df_exports['Descripción Arancelaria'].apply(lambda x: x[:50])

        # Data to plot
        df_plot = df_exports.groupby('Descripción Arancelaria Corta')[["Total valor FOB doláres de la posición"]].sum()
        df_plot = df_plot.sort_values(by='Total valor FOB doláres de la posición', ascending=False).reset_index().head(
            10)

        # Barplot
        #fig = px.bar(df_plot, x='Total valor FOB doláres de la posición', y='Descripción Arancelaria Corta')
    # For dataset of imports
    elif data == 2:
        # Adjusting character values
        df_imports['Descripción Arancelaria'] = df_imports['Descripción Arancelaria'].astype(str)
        df_imports['Descripción Arancelaria Corta'] = df_imports['Descripción Arancelaria'].apply(lambda x: x[:50])

        # Data to plot
        df_plot = df_imports.groupby('Descripción Arancelaria Corta')[["Valor CIF dólares de la mercancía"]].sum()
        df_plot = df_plot.sort_values(by='Valor CIF dólares de la mercancía', ascending=False).reset_index().head(10)
        # Barplot
        #fig = px.bar(df_plot, x='Valor CIF dólares de la mercancía', y='Descripción Arancelaria Corta')

    return df_plot

df=barplot_10_top(1,249,25,"", 2021, "Mayo", 2021, "Mayo")
print(df.head(4))
fig=px.bar(df, x='Total valor FOB doláres de la posición', y='Descripción Arancelaria Corta')
fig.show()