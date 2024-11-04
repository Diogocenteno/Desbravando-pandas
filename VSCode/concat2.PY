# Importando as bibliotecas necessárias
import pandas as pd
import os

#%%

# Carregando o arquivo de homicídios e renomeando a coluna 'valor' para 'homicidios'
df_01 = pd.read_csv('../data/ipea/homicidios.csv', sep=';')
df_01 = df_01.rename(columns={'valor':'homicidios'})
df_01

#%%

# Carregando o arquivo de homicídios de mulheres por armas de fogo e renomeando a coluna 'valor' para 'homicidios-de-mulheres-por-armas-de-fogo'
df_02 = pd.read_csv('../data/ipea/homicidios-de-mulheres-por-armas-de-fogo.csv', sep=';')
df_02 = df_02.rename(columns={'valor':'homicidios-de-mulheres-por-armas-de-fogo'})
df_02

#%%

# Configurando o índice para as colunas 'cod', 'nome' e 'período' para ambos os DataFrames
df_01 = df_01.set_index(['cod', 'nome', 'período'])
df_02 = df_02.set_index(['cod', 'nome', 'período'])
df_01
df_02


#%%

# Concatenando os DataFrames df_01 e df_02 com base no índice e resetando o índice para transformá-los em colunas
pd.concat([df_01, df_02], axis=1).reset_index()


# SEGUNDA OPÇÃO E MELHOR
#%%

# Função para importar e realizar ETL (extração, transformação e carga) nos arquivos CSV
def import_etl(path: str):
    # Extraindo o nome do arquivo sem a extensão
    name = path.split("/")[-1].split(".")[0]

    # Carregando o DataFrame
    df = pd.read_csv(path, sep=';')

    # Verificando se as colunas necessárias estão presentes
    expected_columns = ["cod", "nome", "período"]
    if not all(col in df.columns for col in expected_columns):
        print(f"Arquivo {name} não contém todas as colunas esperadas: {expected_columns}")
        return None

    # Renomeando a coluna 'valor' e configurando o índice
    df = df.rename(columns={"valor": name}).set_index(expected_columns)

    return df
    

#SALVAR ARQUIVO
#%%
# Definindo o caminho dos arquivos e listando os arquivos no diretório
path = "../data/ipea/"
files = os.listdir(path)

# Criando uma lista para armazenar os DataFrames carregados
dfs = []
for i in files:
    df = import_etl(path + i)
    if df is not None:  # Adicionando apenas DataFrames válidos
        dfs.append(df)

# Concatenando todos os DataFrames na lista dfs e resetando o índice
df_DIOGO2 = pd.concat(dfs, axis=1).reset_index()

# Salvando o DataFrame consolidado em um novo arquivo CSV
df_DIOGO2.to_csv("../data/DIOGO2_consolidado.csv", sep=";", index=False)

# Exibindo o DataFrame consolidado
print(df_DIOGO2)

#%%
