#%% 
# Data Importing

# Lê arquivos em formato CSV
df = pd.read_csv("caminho/para/seu_arquivo.csv")  # Utilizado para importar dados de arquivos CSV

# Lê arquivos delimitados por tabulações ou outros delimitadores
df = pd.read_table("caminho/para/seu_arquivo.txt")  # Utilizado para importar dados de arquivos delimitados

# Lê planilhas Excel em diferentes formatos (.xls, .xlsx)
df = pd.read_excel("caminho/para/seu_arquivo.xlsx")  # Utilizado para importar dados de arquivos Excel

# Executa consultas SQL e importa os dados para um DataFrame
# Exemplo: df = pd.read_sql(query, conexão)
df = pd.read_sql("SUA_QUERY_SQL", "sua_conexao")  # Utilizado para importar dados de bancos de dados SQL

# Lê arquivos em formato JSON e converte em DataFrame
df = pd.read_json("caminho/para/seu_arquivo.json")  # Utilizado para importar dados de arquivos JSON

# Extrai tabelas de arquivos HTML
df = pd.read_html("caminho/para/seu_arquivo.html")  # Utilizado para importar dados de tabelas em arquivos HTML

# Cria um DataFrame a partir de listas, dicionários ou arrays
df = pd.DataFrame(data={"coluna1": [1, 2], "coluna2": [3, 4]})  # Utilizado para criar um novo DataFrame

# Junta DataFrames em um só, concatenando-os
df = pd.concat([df1, df2])  # Utilizado para concatenar DataFrames

# Cria uma Series (estrutura unidimensional) no Pandas
s = pd.Series([1, 2, 3, 4])  # Utilizado para criar uma nova Series

# Gera uma sequência de datas em um intervalo específico
df = pd.date_range(start='2023-01-01', end='2023-01-10')  # Utilizado para criar uma sequência de datas

#%% 
# Data Cleaning
# Preenche valores ausentes (NaN) com um valor especificado
df.fillna(value=0, inplace=True)  # Utilizado para substituir NaNs por um valor

# Remove linhas ou colunas com valores ausentes
df.dropna(inplace=True)  # Utilizado para remover NaNs do DataFrame

# Ordena o DataFrame com base nos valores de uma coluna
df.sort_values(by='coluna', inplace=True)  # Utilizado para ordenar o DataFrame

# Aplica uma função a cada elemento do DataFrame
df['coluna'] = df['coluna'].apply(lambda x: x * 2)  # Utilizado para aplicar funções aos dados

# Agrupa os dados em grupos com base em uma ou mais colunas
df_grouped = df.groupby(['coluna1']).sum()  # Utilizado para agregar dados em grupos

# Anexa linhas de outro DataFrame ao final do atual
df = df.append(df2, ignore_index=True)  # Utilizado para adicionar linhas a um DataFrame

# Junta DataFrames com base em uma chave comum
df = df.merge(df2, how='left', left_on='id', right_on='id_user')  # Utilizado para unir DataFrames

# Altera os rótulos das colunas ou linhas no DataFrame
df.rename(columns={'old_name': 'new_name'}, inplace=True)  # Utilizado para renomear colunas ou índices

# Exporta o DataFrame para um arquivo CSV
df.to_csv("caminho/para/arquivo.csv", index=False)  # Utilizado para salvar o DataFrame como CSV

# Define uma coluna como índice do DataFrame
df.set_index('coluna', inplace=True)  # Utilizado para definir um índice no DataFrame

#%% 
# Data Statistic
# Retorna as primeiras n linhas do DataFrame
df.head(5)  # Utilizado para visualizar as primeiras linhas

# Retorna as últimas n linhas do DataFrame
df.tail(5)  # Utilizado para visualizar as últimas linhas

# Gera estatísticas descritivas resumidas para o DataFrame
df.describe()  # Utilizado para obter estatísticas descritivas

# Exibe informações sobre o DataFrame, como número de entradas e tipos de dados
df.info()  # Utilizado para visualizar informações gerais do DataFrame

# Calcula a média para cada coluna numérica
mean_values = df.mean()  # Utilizado para calcular a média das colunas numéricas

# Calcula a mediana para cada coluna numérica
median_values = df.median()  # Utilizado para calcular a mediana das colunas numéricas

# Conta o número de entradas não nulas para cada coluna
count_values = df.count()  # Utilizado para contar entradas não nulas

# Calcula o desvio padrão para cada coluna numérica
std_values = df.std()  # Utilizado para calcular o desvio padrão das colunas numéricas

# Retorna o valor máximo para cada coluna numérica
max_values = df.max()  # Utilizado para encontrar o valor máximo

# Retorna o valor mínimo para cada coluna numérica
min_values = df.min()  # Utilizado para encontrar o valor mínimo

#%%