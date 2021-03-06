from controller import local_to_dataframes as ltd
import plotly.express as px


def lineplot(tipo,FROM_MONTH,FROM_YEAR_EXP,TO_MONTH,TO_YEAR_EXP,PAIS="",DPTO="",POS=""):
    if PAIS==None:
        PAIS=""
    if DPTO==None:
        DPTO=""
    if POS==None:
        POS=""
    else:
        POS=str(POS)
    if FROM_MONTH==None:
        FROM_MONTH="Enero"
    if FROM_YEAR_EXP==None:
        FROM_YEAR_EXP=2020
    if TO_MONTH==None:
        TO_MONTH="Diciembre"
    if TO_YEAR_EXP==None:
        TO_YEAR_EXP=2020
    print("AAAAAAAAAAAAAAAAAAAAAAa")
    print(tipo,FROM_MONTH,FROM_YEAR_EXP,TO_MONTH,TO_YEAR_EXP,PAIS,DPTO,POS)
    print(type(POS))

    df_exports, df_imports=ltd.dataframes_all_lineplot(FROM_YEAR_EXP, FROM_MONTH, TO_YEAR_EXP, TO_MONTH,PAIS, DPTO, POS)
    print(df_exports.info())
    print(df_imports.info())
    if tipo==1:
        df=df_exports

        if POS != "":
            df=df.groupby(by=["Mes","Año","Posición Arancelaria"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
            df.sort_values(by=["Año","Mes"], inplace=True)
            df["Fecha"] = df["Mes"].astype(str) + "-" + df["Año"].astype(str)
            df.drop(index=df.index[df["Total valor FOB doláres de la posición"] == 0], inplace=True)
            fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición", labels={"FOBDOL": "Valor FOB (USD)"})
        else:
            df=df.groupby(by=["Mes","Año"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
            df.sort_values(by=["Año","Mes"], inplace=True)
            df["Fecha"] = df["Mes"].astype(str) + "-" + df["Año"].astype(str)
            df.drop(index=df.index[df["Total valor FOB doláres de la posición"] == 0], inplace=True)
            fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición",labels={"FOBDOL": "Valor FOB (USD)"})

    else:
        if tipo == 2:
            df=df_imports
            if POS != "":
                df=df.groupby(by=["Mes","Año","Posición arancelaria"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
                df.sort_values(by=["Año", "Mes"], inplace=True)
                df["Fecha"] = df["Mes"].astype(str) + "-" + df["Año"].astype(str)
                df.drop(index=df.index[df["Valor CIF dólares de la mercancía"] == 0], inplace=True)
                fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})
            else:
                df=df.groupby(by=["Mes","Año"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
                df.sort_values(by=["Año", "Mes"], inplace=True)
                df["Fecha"] = df["Mes"].astype(str) + "-" + df["Año"].astype(str)
                df.drop(index=df.index[df["Valor CIF dólares de la mercancía"] == 0], inplace=True)
                fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})

    return fig
