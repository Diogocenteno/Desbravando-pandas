#%% 
# Importando a biblioteca pandas
import pandas as pd 

#%% 
# Carregando os dados de transações a partir de um arquivo Excel
df = pd.read_excel("../data/transactions.xlsx")
df  # Exibindo o DataFrame para verificar os dados carregados

#%% 
# Filtrando dados de um cliente específico usando uma condição
# Seleciona todas as transações de um cliente específico (IdCustomer) e calcula o total de pontos
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condicao]
df_user['Points'].sum()  # Calcula a soma de pontos do cliente filtrado

#%% 
# Método menos eficiente para calcular pontos por cliente
# Cria um dicionário com o total de pontos para cada cliente (usando um loop for)
pontos = {}
for i in df['IdCustomer'].unique():
    condicao = df['IdCustomer'] == i
    pontos[i] = df[condicao]['Points'].sum()
pontos  # Exibe o dicionário com os pontos por cliente 

#%% 
# Método mais eficiente para calcular pontos por cliente usando groupby
# Agrupa os dados por IdCustomer e calcula a soma de pontos para cada cliente
df_summary = df.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()  # Reseta o índice para transformar IdCustomer em uma coluna

#%% 
# Agregação de múltiplas métricas usando groupby
# Agrupa os dados por IdCustomer e calcula a soma de pontos, a contagem de UUID e a última data de transação
(df.groupby(['IdCustomer'])
   .agg({'Points': 'sum', 
         'UUID': 'count',
         'DtTransaction': 'max',
         })
   .rename(columns={
       'Points': 'Valor',
        'UUID': 'Frequencia',
        'DtTransaction': 'UltimaData'
        })
    .reset_index()
   )  # Exibe o DataFrame com as métricas agregadas


#%% 
# Importando o módulo datetime para manipulação de datas
import datetime

#%% 
# Calculando a diferença de tempo entre a data atual e a primeira data de transação
datetime.datetime.now() - df['DtTransaction'][0]  # Retorna um objeto timedelta representando a diferença entre a data atual e a primeira data de transação


#%%
# Definindo a primeira data de transação e a data atual
data1 = df['DtTransaction'][0]  # Obtém a data da primeira transação no DataFrame
now = datetime.datetime.now()  # Obtém a data e hora atual

# Calculando a diferença em dias entre a data atual e a data da transação
(now - data1).days  # Retorna o número de dias de diferença entre as duas datas

#%% 
# Definindo uma função para calcular a recência das transações
def recencia(x):
    # Calcula a diferença em dias entre a data atual e a última data de transação
    diff = datetime.datetime.now() - df['DtTransaction'].max()
    return diff.days  # Retorna o número de dias desde a última transação

# Agrupando os dados por IdCustomer e calculando várias métricas
(df.groupby(['IdCustomer'])
   .agg({
       'Points': 'sum',  # Soma total de pontos por cliente
       'UUID': 'count',  # Contagem de transações (UUID) por cliente
       'DtTransaction': ['max', recencia]  # Última data de transação e recência
   })
   .rename(columns={
       'Points': 'Valor',  # Renomeando a coluna de soma de pontos para 'Valor'
       'UUID': 'Frequencia',  # Renomeando a coluna de contagem de UUID para 'Frequencia'
       'DtTransaction': 'UltimaData'  # Renomeando a coluna de data para 'UltimaData'
   })
   .reset_index()  # Reseta o índice para que IdCustomer seja uma coluna do DataFrame resultante
)


#%%

def recencia(last_transaction):
    # Calcula a diferença em dias entre a data atual e a última data de transação
    diff = datetime.datetime.now() - last_transaction
    return diff.days  # Retorna o número de dias desde a última transação

# Agrupando os dados por IdCustomer e calculando várias métricas
result = (df.groupby(['IdCustomer'])
   .agg({
       'Points': 'sum',  # Soma total de pontos por cliente
       'UUID': 'count',  # Contagem de transações (UUID) por cliente
       'DtTransaction': 'max'  # Última data de transação
   })
   .rename(columns={
       'Points': 'Valor',  # Renomeando a coluna de soma de pontos para 'Valor'
       'UUID': 'Frequencia',  # Renomeando a coluna de contagem de UUID para 'Frequencia'
       'DtTransaction': 'UltimaData'  # Renomeando a coluna de data para 'UltimaData'
   })
   .reset_index()  # Reseta o índice para que IdCustomer seja uma coluna do DataFrame resultante
)

# Calculando a recência
result['Recencia'] = result['UltimaData'].apply(recencia)
print(result)

#%%