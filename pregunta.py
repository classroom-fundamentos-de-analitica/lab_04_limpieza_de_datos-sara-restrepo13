"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop(['Unnamed: 0'],axis=1,inplace=True)
    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(inplace=True)

    df["sexo"]=df['sexo'].str.upper()
    df["tipo_de_emprendimiento"]=df["tipo_de_emprendimiento"].str.upper()
    df["tipo_de_emprendimiento"]=df["tipo_de_emprendimiento"].str.replace(' ','')
    df["idea_negocio"]=df["idea_negocio"].str.upper()
    df["idea_negocio"]=df["idea_negocio"].str.replace(' ','_')
    df["idea_negocio"]=df["idea_negocio"].str.replace('-','_')
    df["barrio"]=df["barrio"].str.upper()
    df["barrio"]=df["barrio"].str.replace('-',' ')
    df["barrio"]=df["barrio"].str.replace('_',' ')
    df["estrato"]=df['estrato'].astype('category')
    df["comuna_ciudadano"]=df['comuna_ciudadano'].astype('category')
    df["monto_del_credito"]=df['monto_del_credito'].str.replace(',','')
    df["monto_del_credito"]=df['monto_del_credito'].str.replace('.00','')
    df["monto_del_credito"]=df['monto_del_credito'].str.replace('.','')
    df["monto_del_credito"]=df['monto_del_credito'].str.strip('$')
    df["monto_del_credito"]=df['monto_del_credito'].astype('float')
    df["línea_credito"]=df["línea_credito"].str.upper()
    df["línea_credito"]=df["línea_credito"].str.replace(' ','_')
    df["línea_credito"]=df["línea_credito"].str.replace('-','_')

    #Cambio de Fechas
    def Fecha(x):
        try:
            return datetime.strptime(x,'%d/%m/%Y')
        except:
            return datetime.strptime(x,'%Y/%m/%d')
                                 
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: Fecha(x))
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%d/%m/%Y')

    df.dropna(axis=0,inplace=True)
    df.drop_duplicates(inplace=True)

    return df

print(clean_data())