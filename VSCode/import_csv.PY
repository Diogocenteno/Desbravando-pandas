#%% 
# Importando a biblioteca pandas para manipulação de dados e carregando o arquivo CSV
import pandas as pd

#%% 
# Carregar o arquivo CSV com separador ';' e armazená-lo no DataFrame `df_customers`
df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

#%% 
# Verificando a quantidade de linhas e colunas do DataFrame
df_customers.shape

#%% 
# Exibindo informações gerais sobre o DataFrame, incluindo uso de memória
df_customers.info(memory_usage='deep')

#%% 
# Exibindo uma análise estatística da coluna 'Points'
df_customers['Points'].describe()

#%% 
# Encontrando o valor máximo de pontos
maximo = df_customers['Points'].max()
maximo

#%% 
# Filtrando os dados para obter as linhas onde a pontuação é máxima
maximo = df_customers['Points'].max()
condicao = df_customers['Points'] == maximo
df_customers[condicao]

#%% 
# Extraindo o nome do cliente com a pontuação máxima
condicao = df_customers['Points'] == df_customers['Points'].max()
df_maior = df_customers[condicao]
df_maior['Name'].iloc[0]

#%% 
# Encontrando o valor mínimo de pontos
minimo = df_customers['Points'].min()
minimo

#%% 
# Filtrando os dados para obter as linhas onde a pontuação é mínima
minimo = df_customers['Points'].min()
condicao = df_customers['Points'] == minimo
df_customers[condicao]

#%% 
# Exibindo as notas maiores que 5 de uma lista de notas
notas = [4.5, 6, 7, 3.5]
for i in notas:
    if i > 5:
        print(i)

#%% 
# Adicionando 1 a cada nota na lista e armazenando em `notas_novas`
notas_novas = []
for i in notas:
    notas_novas.append(i + 1)
    
notas_novas

#%% 
# Adicionando 1000 pontos a todos os valores na coluna 'Points'
df_customers['Points'] + 1000

#%% 
# Subtraindo 1000 pontos de todos os valores na coluna 'Points'
df_customers['Points'] - 1000

#%% 
# Multiplicando todos os valores na coluna 'Points' por 2
df_customers['Points'] * 2

#%% 
# Dividindo todos os valores na coluna 'Points' por 2
df_customers['Points'] / 2

#%% 
# Criando um histograma dos valores da coluna 'Points'
df_customers['Points'].plot(kind='hist')

#%% 
# Criando uma densidade de distribuição dos valores da coluna 'Points'
df_customers['Points'].plot(kind='density')

#%% 
# Filtrando clientes com pontuação superior a 1000
condicao = df_customers['Points'] > 1000
df_customers[condicao]

#%% 
# Filtrando clientes com pontuação inferior a 1000
condicao = df_customers['Points'] < 1000
df_customers[condicao]

#%% 
# Filtrando clientes com pontuação entre 1000 e 2000
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_customers[condicao]

#%% 
# Criando uma cópia dos dados filtrados com pontuação entre 1000 e 2000 e adicionando 1000 pontos
condicao = (df_customers['Points'] >= 1000) & (df_customers['Points'] <= 2000)
df_1000_2000 = df_customers[condicao].copy()

df_1000_2000['Points'] = df_1000_2000['Points'] + 1000
df_1000_2000

#%% 
# Exibindo uma análise estatística dos dados filtrados com pontuação entre 1000 e 2000
df_customers[condicao].describe()

#%% 
# Exibindo apenas as colunas 'UUID' e 'Name'
df_customers[['UUID', 'Name']]

#%% 
# Listando o nome de todas as colunas
df_customers.columns.tolist()

#%% 
# Ordenando as colunas em ordem alfabética e reorganizando o DataFrame
colunas = df_customers.columns.tolist()
colunas.sort()
df_customers = df_customers[colunas]
df_customers

#%% 
# Renomeando as colunas 'Name' para 'Nome', 'Points' para 'Pontos' e 'UUID' para 'Id'
df_customers = df_customers.rename(columns={'Name': 'Nome', 'Points': 'Pontos', 'UUID': 'Id'})
df_customers

#%%
