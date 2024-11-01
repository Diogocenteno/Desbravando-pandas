# %%
import pandas as pd
import numpy as np

# Carregar o DataFrame a partir de um arquivo Excel
df = pd.read_excel("../data/transacao_cartao.xlsx")
df

# %%
# Converter a coluna de datas para o formato datetime
df['dtTransaction'] = pd.to_datetime(df['dtTransaction'],
                                     format='%d/%m/%Y')

df

# %%
# Função para dividir o valor total pela quantidade de parcelas
def fatia_parcelas(row):
    return [row["Valor"]/ row["Parcelas"] for i in range(row["Parcelas"])]

# Aplicar a função e criar uma nova coluna com o valor de cada parcela
df['ValorParcela'] = df.apply(fatia_parcelas, axis=1)

df

# %%
# Explodir a lista de parcelas para criar uma linha por parcela
df_fatura = df.explode("ValorParcela")
df_fatura

# %%
# Remover colunas que não são mais necessárias
df_fatura = df_fatura.drop(['Valor','Parcelas'],
                           axis=1)

df_fatura

# %%
# Adicionar um novo campo que representa a ordem da parcela em meses
df_fatura["Months_add"] = (df_fatura.groupby("idTransaction")["dtTransaction"]
                                    .rank('first')
                                    .astype(int))

df_fatura

# %%
# Função para adicionar meses à data da transação
def add_months(row):
    # Adicionar meses usando pd.DateOffset
    new_date = row["dtTransaction"] + pd.DateOffset(months=row['Months_add'])
    dt_str = new_date.strftime("%Y-%m")  # Formatar a nova data como string no formato 'YYYY-MM'
    return dt_str

#%% 
# Aplicar a função para criar a nova coluna com a data da fatura
df_fatura["DtFatura"] = df_fatura.apply(add_months, axis=1)
df_fatura

#%%
# SALAVAR EM PLANILHA
# Caminho do arquivo Excel onde o DataFrame será salvo
caminho_arquivo = "../data/fatura_cartao.xlsx"

# Exportar o DataFrame para um arquivo Excel
df_fatura.to_excel(caminho_arquivo, index=False)

print(f"DataFrame exportado para {caminho_arquivo} com sucesso!")

#%%


#%%
# Agrupar os dados por cliente e data da fatura, somando o valor das parcelas
df_fatura_mes = (df_fatura.groupby(['idCliente', 'DtFatura'])["ValorParcela"]
                          .sum()
                          .reset_index())
df_fatura_mes

# %%
# Criar uma tabela dinâmica para organizar os dados
df_fatura_mes = (df_fatura_mes.pivot_table(columns="DtFatura",
                                          index="idCliente",
                                          values="ValorParcela")
                              .fillna(0)  # Substituir NaN por 0
                              .reset_index()
                              )

df_fatura_mes

# %%
#SALVAR ARQUIVO
# Exportar o DataFrame final para um arquivo Excel
df_fatura_mes.to_excel("Fatura_detalhada.xlsx")

#%%
