#%%
import pandas as pd

#%% 
# Carregando o arquivo 'customers.csv' em um DataFrame, com separador ponto e vírgula (';')
df = pd.read_csv('../data/customers.csv', sep=';')
df

#%% 
# Ordenando o DataFrame pelos valores das colunas 'Points' em ordem decrescente e 'Name' em ordem alfabética ascendente
# Exibindo as últimas 20 linhas do DataFrame ordenado
df.sort_values(by=['Points', 'Name'], ascending=[False, True]).tail(20)

#%% 
# Ordenando o DataFrame pelos valores das colunas 'Points' em ordem decrescente e 'Name' em ordem alfabética ascendente
# Exibindo as primeiras 20 linhas do DataFrame ordenado
df.sort_values(by=['Points', 'Name'], ascending=[False, True]).head(20)

#%%
# df.sort_values(by='Points', ascending=True, inplace=True) ou df.rename(columns={'UUID': 'Id', 'Name': 'Nome', 'Points': 'Pontos'}, inplace=True) ou df = (df.sort_values(by=['Points', 'Name'], ascending=[False, True]).rename(columns={'UUID': 'Id', 'Name': 'Nome', 'Points': 'Pontos'}))

# Ordenando o DataFrame pela coluna 'Points' em ordem crescente e renomeando as colunas:
# 'UUID' para 'Id', 'Name' para 'Nome', e 'Points' para 'Pontos'
df = df.sort_values(by='Points', ascending=True)
df = df.rename(columns={'UUID': 'Id', 'Name': 'Nome', 'Points': 'Pontos'})
df

#%% 
# Ordenando o DataFrame pela coluna 'Points' em ordem decrescente
df.sort_values(by='Points', ascending=False)

