#%%
import pandas as pd
import sqlalchemy

#%% 
# Criar a conexão com o banco de dados SQLite
engine = sqlalchemy.create_engine('sqlite:///../data/database.db')
engine

#%% 
# Ler a tabela 'customers' diretamente em um DataFrame
df_transactions_cart = pd.read_sql_table('customers', engine)
df_transactions_cart

#%% 
# Melhor forma de ler a tabela, limitando o número de resultados
query = 'SELECT * FROM customers LIMIT 30'
df_customers = pd.read_sql_query(query, engine)
df_customers 

#%% 
# Realizar um JOIN entre as tabelas 'customers' e 'transactions'
query = """
SELECT *
FROM customers AS t1
LEFT JOIN transactions AS t2
ON t1.UUID = t2.IdCustomer
LIMIT 10
"""
df_join = pd.read_sql_query(query, engine)
df_join




#%% 
import pandas as pd
from sqlalchemy import create_engine, inspect

# Conectar ao banco de dados SQLite
engine = create_engine('sqlite:///../data/database.db')

# Criar os dataframes de exemplo
data_01 = {
    "id": [1, 2, 3, 4],
    "nome": ["Teo", "Mat", "Nah", "Mah"],
    "idade": [31, 31, 32, 32]
}
df_01 = pd.DataFrame(data_01)

data_02 = {
    "id": [5, 6, 7, 8],
    "nome": ["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade": [23, 33, 19, 21]
}
df_02 = pd.DataFrame(data_02)

# Usar inspect para verificar se a tabela já existe
inspector = inspect(engine)
if not inspector.has_table("tb_fodase"):
    # Se a tabela não existir, criar com df_01
    df_01.to_sql("tb_fodase", engine, index=False)
else:
    # Se a tabela já existir, adicionar os dados de df_01
    df_01.to_sql("tb_fodase", engine, index=False, if_exists="append")

# Adicionar df_02 à tabela
df_02.to_sql("tb_fodase", engine, index=False, if_exists="append")

# Ler os dados da tabela para verificar os resultados
result = pd.read_sql("tb_fodase", engine)
print(result)

#%%

