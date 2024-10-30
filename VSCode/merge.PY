#%% 
# Importando a biblioteca pandas
import pandas as pd

#%% 
# Criando um dicionário com dados dos usuários
data_users = {
    "id": [1, 2, 3, 4],  # IDs dos usuários
    "nome": ["Teo", "Mat", "Nah", "Mah"],  # Nomes dos usuários
    "idade": [31, 31, 32, 32]  # Idades dos usuários
}

# Criando um DataFrame a partir do dicionário de usuários
df_user = pd.DataFrame(data_users)
df_user  # Exibindo o DataFrame de usuários

#%% 
# Criando um dicionário com dados das transações
data_transacoes = {
    "id_user": [1, 1, 1, 2, 3, 3, 5],  # IDs dos usuários que realizaram as transações
    "vl": [432, 532, 123, 6, 4, 87, 10],  # Valores das transações
    "qtProdutos": [2, 1, 3, 6, 10, 2, 7]  # Quantidade de produtos nas transações
}

# Criando um DataFrame a partir do dicionário de transações
df_transacoes = pd.DataFrame(data_transacoes)
df_transacoes  # Exibindo o DataFrame de transações

#%% 
# Realizando uma junção (merge) à esquerda entre df_user e df_transacoes
# Isso traz todos os usuários e suas transações, mesmo que não tenham realizado nenhuma
df_user.merge(df_transacoes, 
                    how='left', 
                    left_on='id', 
                    right_on='id_user'
                    )

#%% 
# Realizando uma junção (merge) à direita entre df_transacoes e df_user
# Isso traz todas as transações e os usuários correspondentes, mesmo que não estejam listados em df_user
df_transacoes.merge(df_user, 
                    how='right', 
                    left_on='id_user', 
                    right_on='id'
                    )

#%% 
# Realizando uma junção (merge) interna entre df_transacoes e df_user
# Isso traz apenas as transações que têm usuários correspondentes
df_transacoes.merge(df_user,
                   how='inner',
                   left_on=['id_user'],
                   right_on=['id'],
                   )

#%% 
# Realizando uma junção (merge) à esquerda e filtrando usuários sem transações
df_merge = df_transacoes.merge(df_user, 
                    how='left', 
                    left_on='id_user', 
                    right_on='id'
                    )

# Filtrando o DataFrame para exibir apenas os usuários que não têm transações associadas
df_merge[df_merge['nome'].isna()]  

#%%