#%%
import pandas as pd

# Criando um dicionário com os dados
data = {
    'nome': ['Teo', 'jose', 'ana', 'Maria', 'Julia'],
    'sobrenome': ['Calvo', 'Gomes', 'Calvo', 'Calvo', 'Silva'],
    'idade': [25, 30, 28, 22, 27],
    'renda': [5000, 7000, 6000, 4000, 6500],
    }

#%%
# Acessando o primeiro elemento da coluna 'idade'
data['idade'][0]

#%%
# Acessando o quarto elemento da coluna 'nome'
data['nome'][3]

#%%
# Criando um DataFrame a partir do dicionário de dados
df = pd.DataFrame(data)
df.head()  # Visualizando as 5 primeiras linhas do DataFrame

#%%
# Comparando a coluna 'idade' com o valor 25 (retorna uma série booleana)
df['idade'] <= 25

#%%
# Acessando o primeiro valor da coluna 'idade' usando iloc
df['idade'].iloc[0]

#%%
# Acessando o quarto valor da coluna 'nome' usando iloc
df['nome'].iloc[3]

#%%
# Selecionando a coluna 'sobrenome' do DataFrame
df['sobrenome']

#%%
# Acessando o quarto valor da coluna 'sobrenome' usando iloc
df['sobrenome'].iloc[3]

#%%
# Verificando o tipo da coluna 'idade'
type(df['idade'])

#%%
# Selecionando a linha de índice 3 usando iloc
df.iloc[3]

#%%
# Selecionando a linha de índice 3 usando loc
df.loc[3]

#%%
# Acessando o valor da coluna 'idade' na linha de índice 3 usando loc
df.loc[3, 'idade']

#%%
# Acessando o valor da coluna 'sobrenome' na linha de índice 3 usando loc
df.loc[3, 'sobrenome']

#%%
# Exibindo o DataFrame completo
df

#%%
# Acessando o quarto valor da coluna 'nome' usando iloc
df['nome'].iloc[3]

#%%
# Acessando o quarto valor da coluna 'nome' usando loc
df['nome'].loc[3]

#%%
# Exibindo informações do DataFrame (tipos de dados, valores nulos, etc.)
df.info()

#%%
# Exibindo um resumo estatístico das colunas numéricas do DataFrame
df.describe()

#%%
# Exibindo informações detalhadas do DataFrame, incluindo uso de memória
df.info(memory_usage='deep')

#%%
# Exibindo os tipos de dados de cada coluna do DataFrame
df.dtypes

#%%
# Criando um resumo das estatísticas descritivas do DataFrame
sumario = df.describe()


# Acessando a média da coluna 'renda' a partir do resumo estatístico
sumario['renda']['mean']

#%%
# Exibindo as duas primeiras linhas do DataFrame
df.head(2)

#%%
# Exibindo as duas últimas linhas do DataFrame
df.tail(2)

#%%
# Ordenando o DataFrame pela coluna 'idade' em ordem decrescente e exibindo as duas primeiras linhas
df.sort_values(by='idade', ascending=False).head(2)

#%%
# Criando um gráfico de barras da coluna 'renda'
df['renda'].plot(kind='density')

#%%

