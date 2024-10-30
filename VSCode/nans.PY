#%% 
# Importando bibliotecas necessárias
import pandas as pd
import numpy as np

#%% 
# Criando um dicionário com dados, incluindo valores ausentes (NaN)
data = {
    "nome": ["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade": [31, 32, 34, 12, np.nan],
    "renda": [np.nan, 3245, 357, 12432, np.nan],
}

# Convertendo o dicionário para um DataFrame
df = pd.DataFrame(data)
df  # Exibindo o DataFrame para verificação dos dados

#%% 
# Contando valores ausentes na coluna 'idade'
df['idade'].isna().sum()  # Retorna o número de valores ausentes na coluna 'idade'

#%% 
# Contando valores ausentes em cada coluna do DataFrame
df.isna().sum()  # Exibe a contagem de valores ausentes por coluna

#%% 
# Calculando a proporção de valores ausentes em cada coluna
df.isna().mean()  # Exibe a porcentagem de valores ausentes por coluna

#%% 
# Obtendo estatísticas descritivas do DataFrame
df.describe()  # Exibe estatísticas como média, desvio padrão, valores mínimos e máximos para colunas numéricas

#%% 
# Preenchendo valores ausentes com a média das colunas especificadas
# Utilizando a média para preencher NaNs nas colunas 'idade' e 'renda'
df.fillna({
    'idade': df['idade'].mean(),
    'renda': df['renda'].mean(),
           })

#%% 
# Removendo linhas com valores ausentes em 'idade' ou 'renda'
# ou how='all' para remover apenas se todas as colunas especificadas estiverem ausentes
df.dropna(subset=['idade', 'renda'], how='any')

#%% 
# Removendo colunas com menos de 3 valores não nulos
df.dropna(axis=1, thresh=3)  # Mantém apenas as colunas com pelo menos 3 valores não nulos
df

#%%