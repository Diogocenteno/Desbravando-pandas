#%% 
# Importando a biblioteca pandas
import pandas as pd

# Carregando o arquivo de transações em um DataFrame
df = pd.read_excel('../data/transactions.xlsx')
df

#%% 
# Exibindo as primeiras 5 linhas do DataFrame
df.head(5)

#%% 
# Exibindo as últimas 5 linhas do DataFrame
df.tail(5)

#%% 
# Selecionando apenas as colunas de interesse: 'UUID', 'Points', 'IdCustomer', e 'DtTransaction'
colunas = ['UUID', 'Points', 'IdCustomer', 'DtTransaction']
df = df[colunas]
df

#%% 
# Exibindo informações do DataFrame, incluindo o uso de memória
df.info(memory_usage='deep')

#%%
