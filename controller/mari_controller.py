from controller import local_to_dataframes as ld
import plotly.express as px

def lineplot(tipo,pais,dpto,pos,cat,mesini,anoini,mesfin,anofin):
    df_exports, df_imports, df_exports_cundinamarca, df_imports_cundinamarca = ld.cargar_dataframes(anoini,mesini,anofin,mesfin)

    if tipo==1:
        df=df_exports
        if dpto != "":
            df=df[df["Departamento de procedencia"] == dpto]
        if pais != "":
            df=df[df["Código país destino"]==pais]
        if pos != "":
            df=df.groupby(by=["Fecha","Descripción Arancelaria"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
            fig=px.line(df[df["Descripción Arancelaria"]==pos], x="Fecha", y="Total valor FOB doláres de la posición", title=f'Valor FOB (USD) para la posición arancelaria {pos}, país:{pais}, departamento:{dpto}', labels={"FOBDOL": "Valor FOB (USD)"})
        else:
            if pos == "" and  cat!= "":
                df=df.groupby(by=["Fecha","Descriptiva - SCN - NUEVA BASE 2015"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
                fig=px.line(df_plot[df_plot["Descriptiva - SCN - NUEVA BASE 2015"]==cat], x="Fecha", y="Total valor FOB doláres de la posición", title=f'Valor FOB (USD) para la categoría arancelaria {cat}, país:{pais}, departamento:{dpto}', labels={"FOBDOL": "Valor FOB (USD)"})
            else:
                df=df.groupby(by=["Fecha"]).sum()[["Total valor FOB doláres de la posición"]].reset_index()
                fig=px.line(df, x="Fecha", y="Total valor FOB doláres de la posición", title=f'Valor FOB (USD), país:{pais}, departamento:{dpto}', labels={"FOBDOL": "Valor FOB (USD)"})

    elif tipo == "Importaciones":
        df=df_imports
        if dpto != "":
            df=df[df["Departamento del importador"] == dpto]
        if pais != "":
            df=df[df["País de procedencia"]==pais]
        if pos != "":
            df=df.groupby(by=["Fecha","Descripción Arancelaria"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
            fig=px.line(df[df["Descripción Arancelaria"]==pos], x="Fecha", y="Valor CIF dólares de la mercancía", title=f'Valor CIF (USD) para la posición arancelaria {pos}, país:{pais}, departamento:{dpto}', labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})
        else:
            if pos == "" and  cat!= "":
                df=df.groupby(by=["Fecha","Descriptiva - SCN - NUEVA BASE 2015"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
                fig=px.line(df[df["Descriptiva - SCN - NUEVA BASE 2015"]==cat], x="Fecha", y="Valor CIF dólares de la mercancía", title=f'Valor CIF (USD) para la categoría arancelaria {cat}, país:{pais}, departamento:{dpto}', labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})

            else:
                df=df.groupby(by=["Fecha"]).sum()[["Valor CIF dólares de la mercancía"]].reset_index()
                fig=px.line(df, x="Fecha", y="Valor CIF dólares de la mercancía", title=f'Valor CIF (USD), país:{pais}, departamento:{dpto}', labels={"Valor CIF dólares de la mercancía": "Valor CIF (USD)"})
    return fig