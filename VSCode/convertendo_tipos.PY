# %%
# Importando a biblioteca pandas para manipulação de dados
import pandas as pd

# %%
# Lendo um arquivo CSV que contém informações sobre clientes,
# usando o separador ';' para delimitar os campos
df = pd.read_csv('../data/customers.csv', sep=';')
# Exibindo o DataFrame carregado
df

# %%
# Mostrando os tipos de dados de cada coluna no DataFrame
df.dtypes

# %%
# Convertendo a coluna 'Points' para o tipo string, mas não atribuindo a um novo DataFrame
# A conversão não modifica o DataFrame original, a menos que seja atribuída de volta
df['Points'].astype(str)

# %%
# Criando uma nova coluna 'Points_dobble' que é o dobro dos valores na coluna 'Points'
# Aqui, é importante notar que 'Points' deve ser numérico para essa operação
df['Points_dobble'] = df['Points'] * 2

# %%
# Tentando converter as colunas 'Points' e 'Points_dobble' para o tipo float,
# mas isso não altera o DataFrame original, pois o resultado não é atribuído a uma nova coluna
df[['Points', 'Points_dobble']].astype(float)

#%%