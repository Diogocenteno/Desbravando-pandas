# %%
import pandas as pd

# Carrega os dados dos clientes de um arquivo CSV, separando por ponto e vírgula, e armazena em um DataFrame.
df_customer = pd.read_csv('../data/customers.csv', sep=';')
df_customer

# %%
# Carrega os dados das transações de um arquivo Excel e armazena em um DataFrame.
df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions

# %%
# Carrega os dados de transações do carrinho de um arquivo Parquet e armazena em um DataFrame.
df_transactions_product = pd.read_parquet('../data/transactions_cart.parquet')
df_transactions_product

# %%
# Realiza um merge (junção) entre o DataFrame de transações e o DataFrame de clientes.
# A junção é feita com base no campo `IdCustomer` em `df_transactions` e `UUID` em `df_customer`.
# A junção é do tipo `inner`, ou seja, mantém apenas as linhas com correspondência em ambos os DataFrames.
df_join = df_transactions.merge(df_customer,
                                how='inner',
                                left_on='IdCustomer',
                                right_on='UUID',
                                suffixes=['_transacao', '_cliente']
                                )

# Realiza um segundo merge entre o DataFrame resultante e o DataFrame `df_transactions_product`.
# A junção é feita com base no campo `UUID_transacao` em `df_join` e `IdTransaction` em `df_transactions_product`.
# Essa operação cria um DataFrame final com informações de transações, clientes e produtos.
df_join.merge(df_transactions_product,
              how='inner',
              left_on='UUID_transacao',
              right_on='IdTransaction'
              )

# %%
# Consolida os merges em uma única linha para simplificar o código e evitar a necessidade de variáveis temporárias.
df_join = (df_transactions.merge(df_customer,
                                 how='inner',
                                 left_on='IdCustomer',
                                 right_on='UUID',
                                 suffixes=['_transacao', '_cliente'])
                          .merge(df_transactions_product,
                                 how='inner',
                                 left_on='UUID_transacao',
                                 right_on='IdTransaction')
                                 )

df_join  # Exibe o DataFrame final com as junções realizadas.

#%%