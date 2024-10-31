# %%
import pandas as pd

# Cria um dicionário com dados e o transforma em um DataFrame `df_01`.
# Este DataFrame contém informações de ID, nome e idade para um grupo de pessoas.
data_01 = {
    "id": [1, 2, 3, 4],
    "nome": ["Teo", "Mat", "Nah", "Mah"],
    "idade": [31, 31, 32, 32]
}

df_01 = pd.DataFrame(data_01)
df_01  # Exibe o DataFrame `df_01`.

# %%
# Cria um segundo conjunto de dados em forma de dicionário e o transforma em outro DataFrame `df_02`.
# Este DataFrame contém informações semelhantes, mas com IDs, nomes e idades diferentes.
data_02 = {
    "id": [5, 6, 7, 8],
    "nome": ["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade": [23, 33, 19, 21]
}

df_02 = pd.DataFrame(data_02)
df_02  # Exibe o DataFrame `df_02`.

# %%
# Concatena `df_01` e `df_02` verticalmente (axis=0) e redefine o índice para uma sequência contínua.
# O resultado é um único DataFrame que combina as linhas de ambos os DataFrames, com um índice resetado.
pd.concat([df_01, df_02]).reset_index(drop=True)

# %%
# Cria um terceiro DataFrame `df_03` contendo dados de sobrenome e renda.
# Ordena `df_03` primeiro pela coluna `renda` em ordem decrescente e depois por `sobrenome` em ordem alfabética crescente.
data_03 = {
    "sobrenome": ["Calvo", "Silva", "Costa", "Souza"],
    "renda": [3100, 3100, 3200, 3200]
}

df_03 = pd.DataFrame(data_03).sort_values(['renda', 'sobrenome'], ascending=[False, True])
df_03  # Exibe o DataFrame `df_03` ordenado.

# %%
# Realiza a concatenação de `df_01` e `df_03` horizontalmente (axis=1).
# As colunas de `df_03` são anexadas a `df_01`, criando um DataFrame final com informações combinadas de ambos.
pd.concat([df_01, df_03], axis=1)
