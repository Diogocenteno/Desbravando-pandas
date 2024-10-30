# %% 
# Importando a biblioteca pandas
import pandas as pd

# Carregando o arquivo 'transactions.xlsx' em um DataFrame
df = pd.read_excel("../data/transactions.xlsx")
df
# %% 
# Ordenando o DataFrame pela coluna 'DtTransaction' em ordem decrescente 
# e removendo duplicatas na coluna 'IdCustomer', mantendo apenas a primeira ocorrência (mais recente)
df_last = (df.sort_values("DtTransaction", ascending=False)
             .drop_duplicates(subset=['IdCustomer'], keep='first'))

# Calculando e exibindo o número de valores únicos na coluna 'IdCustomer' após a remoção de duplicatas
df_last['IdCustomer'].nunique()

# %% 
# Criando uma condição para filtrar o DataFrame onde o valor na coluna 'IdCustomer' seja igual a '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
# Exibindo as linhas que atendem a esta condição
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]

# %% 
# Filtrando o DataFrame 'df_last' para exibir apenas a linha onde 'IdCustomer' é igual a '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_last[df_last['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']

#%%
