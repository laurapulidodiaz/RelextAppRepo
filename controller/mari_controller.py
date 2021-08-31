from controller import local_to_dataframes as ltd
import plotly.express as px


def lineplot(tipo,FROM_MONTH,FROM_YEAR_EXP,TO_MONTH,TO_YEAR_EXP,PAIS="",DPTO="",POS=""):
    if PAIS==None:
        PAIS=""
    if DPTO==None:
        DPTO=""
    if POS==None:
        POS=""
    if FROM_MONTH==None:
        FROM_MONTH="Enero"
    if FROM_YEAR_EXP==None:
        FROM_YEAR_EXP=2020
    if TO_MONTH==None:
        TO_MONTH="Diciembre"
    if TO_YEAR_EXP==None:
        TO_YEAR_EXP=2020

    df_exports, df_imports=ltd.dataframes_all_lineplot(FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH,PAIS, DPTO, POS)

    if tipo==1:
        df=df_exports

        if POS != "":
            df=df.groupby(by=["Fecha","Descripción Arancelaria"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
            fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición", labels={"FOBDOL": "Valor FOB (USD)"})
        else:
            if POS == "":
                df=df.groupby(by=["Fecha","SCN - BASE 2015"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
                fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición",labels={"FOBDOL": "Valor FOB (USD)"})
            else:
                df=df.groupby(by=["Fecha"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
                fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición",labels={"FOBDOL": "Valor FOB (USD)"})

    elif tipo == "2":
        df=df_imports

        if POS != "":
            df=df.groupby(by=["Fecha","Descripción Arancelaria"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
            fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})
        else:
            if POS == "":
                df=df.groupby(by=["Fecha","SCN - BASE 2015"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
                fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})

            else:
                df=df.groupby(by=["Fecha"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
                fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})
    return fig
