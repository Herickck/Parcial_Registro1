import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')

#Obtencion de los datos de las Columnas
Columna_alcohol = df.alcohol
Columna_pH = df.pH
Columna_azucar = df.residual_sugar
Columna_Citrico = df.citric_acid

#Obtecion de Media de las Columnas
alcohol_media = df.alcohol.median()
pH_media = df.pH.median()
azucar_media = df.residual_sugar.median()
citrico_media = df.citric_acid.median()

#Operaciones para determinar la Calidad
def Calidad(medianas, columnas):
    for posicion, valor in enumerate(columnas):

        if valor >= medianas:
            df.loc[posicion, valor] = "Calidad Alta"
        else:
            df.loc[posicion, valor] = "Calidad Baja"
        respuesta = df.groupby(valor).quality.mean()
    return print(respuesta)

#Menu para escoger que datos ver
def Menu():
    print ("""
    ¿Que desea saber?
    1) Calidad del Alcohol
    2) Calidad del pH
    3) Calidad del Azucar
    4) Calidad del Acido Citrico
    5) Salir""")

#Obtencion de datos para el metodo calidad
def Datos():
    Menu()
    opc = int(input("Selecione Opcion\n"))

    while (opc >0 and opc <5):

        if (opc==1):
            Calidad(alcohol_media, Columna_alcohol)
            opc = int(input("Selecione otra opcion\n"))

        elif (opc==2):
            Calidad(pH_media, Columna_pH)
            opc = int(input("Selecione otra opcion\n"))

        elif (opc==3):
            Calidad(azucar_media, Columna_azucar)
            opc = int(input("Selecione otra opcion\n"))

        elif (opc==4):
            Calidad(citrico_media, Columna_Citrico)
            opc = int(input("Selecione otra opcion\n"))

        else:
            exit 
Datos()