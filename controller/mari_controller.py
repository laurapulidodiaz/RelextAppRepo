from controller import local_to_dataframes as ltd
import plotly.express as px


def lineplot(tipo,FROM_MONTH,FROM_YEAR_EXP,TO_MONTH,TO_YEAR_EXP,PAIS="",DPTO="",POS="",CAT=""):
    if PAIS==None:
        PAIS=""
    if DPTO==None:
        DPTO=""
    if POS==None:
        POS=""
    if CAT==None:
        CAT=""
    if FROM_MONTH==None:
        FROM_MONTH="Mayo"
    if FROM_YEAR_EXP==None:
        FROM_YEAR_EXP=2021
    if TO_MONTH==None:
        TO_MONTH="Mayo"
    if TO_YEAR_EXP==None:
        TO_YEAR_EXP=2021

    df_exports, df_imports=ltd.dataframes_all_filtros(FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH,PAIS, DPTO, POS, CAT)

    if tipo==1:
        df=df_exports

        if POS != "":
            df=df.groupby(by=["Fecha","Descripción Arancelaria"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
            fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición", title=f'Valor FOB (USD) para la posición arancelaria {POS}, país:{PAIS}, departamento:{DPTO}', labels={"FOBDOL": "Valor FOB (USD)"})
        else:
            if POS == "" and  CAT != "":
                df=df.groupby(by=["Fecha","SCN - BASE 2015"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
                fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición", title=f'Valor FOB (USD) para la categoría arancelaria {CAT}, país:{PAIS}, departamento:{DPTO}', labels={"FOBDOL": "Valor FOB (USD)"})
            else:
                df=df.groupby(by=["Fecha"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
                fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición", title=f'Valor FOB (USD), país:{PAIS}, departamento:{DPTO}', labels={"FOBDOL": "Valor FOB (USD)"})

    elif tipo == "2":
        df=df_imports

        if POS != "":
            df=df.groupby(by=["Fecha","Descripción Arancelaria"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
            fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", title=f'Valor CIF (USD) para la posición arancelaria {POS}, país:{PAIS}, departamento:{DPTO}', labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})
        else:
            if POS == "" and  CAT != "":
                df=df.groupby(by=["Fecha","SCN - BASE 2015"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
                fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", title=f'Valor CIF (USD) para la categoría arancelaria {CAT}, país:{PAIS}, departamento:{DPTO}', labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})

            else:
                df=df.groupby(by=["Fecha"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
                fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", title=f'Valor CIF (USD), país:{PAIS}, departamento:{DPTO}', labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})
    return fig
