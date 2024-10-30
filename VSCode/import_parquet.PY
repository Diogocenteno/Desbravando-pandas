#%%

import pandas as pd
df = pd.read_parquet('../data/transactions_cart.parquet')
df

#%%

#%% 
# Exibindo as primeiras 5 linhas do DataFrame
df.head(5)

#%% 
# Exibindo as últimas 5 linhas do DataFrame
df.tail(5)

#%% 
# Selecionando apenas as colunas de interesse: 'UUID', 'Points', 'IdCustomer', e 'DtTransaction'
colunas = ['UUID', 'IdTransaction', 'Product', 'Quantity']
df = df[colunas]
df

#%% 
# Exibindo informações do DataFrame, incluindo o uso de memória
df.info(memory_usage='deep')

#%%