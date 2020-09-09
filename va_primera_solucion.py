import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

alcohol_media = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= alcohol_media:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
df.groupby('alcohol').quality.mean()

print(df.groupby('alcohol').quality.mean())

pH_media = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= pH_media:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
df.groupby('pH').quality.mean()

print(df.groupby('pH').quality.mean())

azucar_media = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= azucar_media:
        df.loc[i, 'residual sugar'] = 'alto'
    else:
        df.loc[i, 'residual sugar'] = 'bajo'
df.groupby('residual sugar').quality.mean()

print(df.groupby('residual sugar').quality.mean())

citrico_media = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= citrico_media:
        df.loc[i, 'citric acid'] = 'alto'
    else:
        df.loc[i, 'citric acid'] = 'bajo'
df.groupby('citric acid').quality.mean()

print(df.groupby('citric acid').quality.mean())