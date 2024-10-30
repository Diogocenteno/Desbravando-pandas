#%% 
# Importando a biblioteca pandas
import pandas as pd

# Carregando o arquivo 'products.csv' em um DataFrame, 
# especificando o separador como ponto e vírgula (';') 
# e definindo os nomes das colunas como 'Id', 'Name', e 'Description'
df = pd.read_csv('../data/products.csv',
                 sep=';',
                 names=['Id', 'Name', 'Description']
                 )
df

#%% 
# Renomeando as colunas 'Name' para 'Nomes' e 'Description' para 'Descricao'
df = df.rename(columns={'Name': 'Nomes', 'Description': 'Descricao'})
df


#%%