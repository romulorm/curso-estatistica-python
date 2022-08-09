import pandas as pd

dados = {
    'A': [1, 22, 1, 90],
    'B': [40, 45, 47, 49],
    'C': [15, 22, 33, 4]
}

df = pd.DataFrame(dados)
print(df)

# Valores máximos por coluna
df_max = df.max()
print(df_max)

# Valores máximos por linha
df_max_linha = df.max(axis=1)
print(df_max_linha)

# Soma
df_sum = df.sum()
print(df_sum)

# Média
df_media = df.mean()
print(df_media)

# Variância
df_variancia = df.var()
print(df_variancia)

# Desvio padrão
df_desviopadrao = df.std()
print(df_desviopadrao)

# Desvio médio absoluto
df_desviomedioabsoluto = df.mad()
print(df_desviomedioabsoluto)

# Sumário estatístico

df_sumario = df.describe()
print(df_sumario)