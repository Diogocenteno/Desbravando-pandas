# %%
# Importando as bibliotecas pandas e numpy para manipulação de dados e operações numéricas
import pandas as pd
import numpy as np

# %%
# Lendo um arquivo CSV que contém informações sobre clientes,
# usando o separador ';' para delimitar os campos
df = pd.read_csv('../data/customers.csv', sep=';')
# Exibindo o DataFrame carregado
df

# %%
# Criando uma nova coluna 'Points_double' que é o dobro dos valores na coluna 'Points'
df['Points_double'] = df['Points'] * 2

# %%
# Criando uma nova coluna 'Points_ratio' que é a razão entre 'Points_double' e 'Points'
df['Points_ratio'] = df['Points_double'] / df['Points']
df

# %%
# Adicionando uma nova coluna 'Constante' que contém valores nulos
df['Constante'] = None
df 

# %%
# Calculando o logaritmo natural dos valores na coluna 'Points' 
# e armazenando na nova coluna 'Points_log'
df['Points_log'] = np.log(df['Points'])
df

# %%
# Calculando o logaritmo natural das colunas 'Points', 'Points_double' e 'Points_ratio'
# Este resultado não é armazenado em um DataFrame
np.log(df[['Points', 'Points_double', 'Points_ratio']])

# %%
# Convertendo todos os nomes na coluna 'Name' para letras maiúsculas
nomes_alta = []
for i in df['Name']:
    nomes_alta.append(i.upper())
# Armazenando os nomes convertidos em uma nova coluna 'Nome_Alta'
df['Nome_Alta'] = nomes_alta
df

# %%
# Usando a função str.upper() para converter os nomes para maiúsculas
# Esta operação não altera o DataFrame original, pois não está sendo atribuída a nenhuma coluna
df['Name'].str.upper()

# %%
# Definindo uma função que retorna o primeiro elemento de uma string separada por '_'
def get_first(nome: str):
    return nome.split('_')[0]

# %%
# Aplicando a função get_first na coluna 'Name' e armazenando o resultado em uma nova coluna 'Name_First'
df['Name_First'] = df['Name'].apply(get_first)
df

# %%
# Usando uma função lambda para obter o primeiro elemento de 'Name' em maiúsculas
df['Name'].apply(lambda x: x.upper().split('_')[0])

# %%
# Definindo uma função que categoriza os pontos em intervalos
def intervalo_pontos(pontos):
    if pontos < 2500:
        return 'baixo'
    elif pontos < 3500:
        return 'medio'
    else:
        return 'alto'
# Aplicando a função intervalo_pontos na coluna 'Points' e armazenando o resultado em 'Faixa_Pontos'
df['Faixa_Pontos'] = df['Points'].apply(intervalo_pontos)
df

# %%
# Extraindo os últimos três caracteres da coluna 'UUID' usando uma função lambda
df['UUID'].apply(lambda x: x[-3:])

# %%
# Criando um dicionário com dados sobre clientes para um DataFrame
data = {
    "nome": ["Teo", "Nah", "Maria", "Lara"],
    "recencia": [1, 30, 10, 45],
    "valor": [100, 2000, 15, 500],
    "frequencia": [2, 5, 1, 15]
}
# Criando um DataFrame a partir do dicionário
df_crm = pd.DataFrame(data)
df_crm

# Se a recencia <=10: NOTA 10
# Se a recencia > 10 e < 30:NOTA 5
# Se a recencia > 30: NOTA 0

# Se a valor > 1000: NOTA 10
# Se a valor < 1000 e > 100: NOTA 5
# Se a vaslor < 100 : NOTA 0

# Se a frequencia > 10: NOTA 10
# Se a frequencia < 10 e > 5: NOTA 5
# Se a frequencia < 5 : NOTA 0

# Definindo a função que calcula a nota RFV
def rfv(row):
    nota = 0
    
    # Avaliando a recência
    if row['recencia'] <= 10:
        nota += 10
    elif 10 < row['recencia'] <= 30:
        nota += 5
    elif row['recencia'] > 30:
        nota += 0

    # Avaliando o valor
    if row['valor'] > 1000:
        nota += 10
    elif 100 <= row['valor'] < 1000:
        nota += 5
    elif row['valor'] < 100:
        nota += 0

    # Avaliando a frequência
    if row['frequencia'] > 10:
        nota += 10
    elif 5 <= row['frequencia'] < 10:
        nota += 5
    elif row['frequencia'] < 5:
        nota += 0
    
    return nota

# %%
# Aplicando a função rfv ao DataFrame df_crm para calcular a nota RFV e armazenando na nova coluna 'RFV'
df_crm["RFV"] = df_crm.apply(rfv, axis=1)
df_crm

# %%
# Exibindo a primeira linha do DataFrame df_crm
df_crm.iloc[0]

# %%
# Exibindo a segunda linha do DataFrame df_crm
df_crm.iloc[1]

# %%
# Exibindo a terceira linha do DataFrame df_crm
df_crm.iloc[2]

# %%
# Exibindo a quarta linha do DataFrame df_crm
df_crm.iloc[3]



#%%