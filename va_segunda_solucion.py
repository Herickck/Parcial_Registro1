import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')


def Calidad(medianas, columnas):
    for posicion, valor in enumerate(columnas):
        if valor >= medianas:
            df.loc[posicion, valor] = "Calidad Alta"
        else:
            df.loc[posicion, valor] = "Calidad Baja"
        respuesta = df.groupby(valor).quality.mean()
    return print(respuesta)

Calidad(df.alcohol.median(), df.alcohol)
Calidad(df.pH.median(), df.pH)
Calidad(df.residual_sugar.median(), df.residual_sugar)
Calidad(df.citric_acid.median(), df.citric_acid)