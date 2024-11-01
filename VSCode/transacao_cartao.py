# %%
# Importando bibliotecas pandas e numpy para manipulação de dados e cálculos
import pandas as pd
import numpy as np

# Carregando o arquivo Excel contendo as informações de transações com cartão e exibindo o DataFrame resultante
df = pd.read_excel("../data/transacao_cartao.xlsx")
df

# %%
# Convertendo a coluna 'dtTransaction' para o formato de data, especificando o formato original dia/mês/ano
df['dtTransaction'] = pd.to_datetime(df['dtTransaction'], format='%d/%m/%Y')
df

# %%
# Definindo uma função para dividir o valor total da transação pelas parcelas e distribuir o valor de cada parcela igualmente
def fatia_parcelas(row):
    return [row["Valor"] / row["Parcelas"] for i in range(row["Parcelas"])]

# Aplicando a função ao DataFrame para criar uma nova coluna 'ValorParcela', que contém uma lista dos valores de cada parcela
df['ValorParcela'] = df.apply(fatia_parcelas, axis=1)
df

# %%
# Utilizando o método explode para expandir cada lista de parcelas em linhas individuais, criando uma linha para cada parcela
df_fatura = df.explode("ValorParcela")
df_fatura

# %%
# Removendo as colunas 'Valor' e 'Parcelas', que não são mais necessárias após a criação das linhas individuais para cada parcela
df_fatura = df_fatura.drop(['Valor', 'Parcelas'], axis=1)
df_fatura

# %%
# Criando uma coluna 'Months_add' que incrementa a data de cada parcela de acordo com a ordem da parcela dentro da transação
df_fatura["Months_add"] = (df_fatura.groupby("idTransaction")["dtTransaction"]
                                    .rank('first')
                                    .astype(int))
df_fatura

# %%
# Definindo uma função para adicionar o número de meses apropriado a cada parcela, e retornando a nova data no formato "Ano-Mês"
def add_months(row):
    new_date = row["dtTransaction"] + np.timedelta64(row['Months_add'], 'M')
    dt_str = new_date.strftime("%Y-%m")
    return dt_str

# Aplicando a função para criar a coluna 'DtFatura' que representa o mês de vencimento de cada parcela
df_fatura["DtFatura"] = df_fatura.apply(add_months, axis=1)
df_fatura

# %%
# Agrupando o DataFrame pelo cliente e pela data de faturamento (DtFatura) e somando o valor das parcelas de cada mês
df_fatura_mes = (df_fatura.groupby(['idCliente', 'DtFatura'])["ValorParcela"]
                          .sum()
                          .reset_index())
df_fatura_mes

# %%
# Convertendo o DataFrame para uma tabela com datas de faturamento como colunas, clientes como linhas e valores de parcelas como valores
df_fatura_mes = (df_fatura_mes.pivot_table(columns="DtFatura",
                                          index="idCliente",
                                          values="ValorParcela")
                              .fillna(0)   # Substitui valores ausentes por zero
                              .reset_index())
df_fatura_mes

# %%
# Exportando o DataFrame resultante para um arquivo Excel chamado "Fatura_detalhada.xlsx"
df_fatura_mes.to_excel("Fatura_detalhada.xlsx")

# %%
