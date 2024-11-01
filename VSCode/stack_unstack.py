# %%
# Importando a biblioteca pandas para manipulação de dados
import pandas as pd

# Lendo um arquivo CSV, utilizando ponto e vírgula como delimitador, e exibindo o dataframe carregado
df = pd.read_csv("../data/bia_consolidado.csv", sep=";")
df

# %%
# Definindo uma combinação de colunas ("cod", "nome", "período") como índice do dataframe
df = df.set_index(["cod", "nome", "período"])
df

# %%
# Transformando o dataframe para o formato empilhado (long format) para reorganizar os dados
# "level_3" representa o tipo de homicídio e "0" representa a quantidade
df_stack = df.stack().reset_index().rename(columns={"level_3": "Tipo Homicidio", 0: "Qtde"})

df_stack

# %%
# Convertendo o dataframe de volta para o formato original (wide format) com a quantidade separada por tipo de homicídio
df_unstack = (df_stack.set_index(['cod', 'nome', 'período', 'Tipo Homicidio'])
                      .unstack()
                      .reset_index())

df_unstack

# %%
# Extraindo os nomes das colunas de quantidades e identificadores para reorganizar o dataframe
homicidios = df_unstack['Qtde'].columns.tolist()  # Obtendo as colunas de quantidade de homicídios
indentificadores = df_unstack.columns.droplevel(1).tolist()[:3]  # Extraindo as colunas de identificação (cod, nome, período)

# Renomeando as colunas do dataframe para juntar identificadores e categorias de homicídio
df_unstack.columns = indentificadores + homicidios
df_unstack

# %%
