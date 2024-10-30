#%% 
# Importando a biblioteca pandas
import pandas as pd

# Criando um dicionário com dados de exemplo e convertendo-o em um DataFrame
data = {
    "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
    "Idade": [32, 33, 2, 33, 31, 32],
    "updated_at": [1, 2, 3, 1, 2, 3]
}
df = pd.DataFrame(data)
df

#%% 
# Ordenando o DataFrame pela coluna 'updated_at' em ordem decrescente, sem modificar 'df' diretamente
df.sort_values(by="updated_at", ascending=False)
df

#%% 
# Removendo duplicatas no DataFrame com base nas colunas 'Nome' e 'Idade', mantendo apenas a primeira ocorrência de cada duplicata
df.drop_duplicates(subset=["Nome", "Idade"], keep='first')
df

# %% 
# Ordenando o DataFrame pela coluna 'updated_at' em ordem decrescente e, em seguida, 
# removendo duplicatas nas colunas 'Nome' e 'Idade', mantendo apenas a primeira ocorrência.
# Atribuindo o resultado final a 'df'
df = (df.sort_values(by="updated_at", ascending=False)
        .drop_duplicates(subset=["Nome", "Idade"], keep='first'))

df

#%%
# Removendo duplicatas no DataFrame com base nas colunas 'Nome' e 'Idade'
# Pode ser feito das seguintes maneiras:

# 1. Utilizando a função drop_duplicates e atribuindo o resultado de volta a 'df'
df = df.drop_duplicates(subset=["Nome", "Idade"])

# Ou, alternativamente:

# 2. Usando a função drop_duplicates diretamente sem atribuir a 'df' novamente, o que não altera o DataFrame original
df.drop_duplicates(subset=["Nome", "Idade"])

#%%