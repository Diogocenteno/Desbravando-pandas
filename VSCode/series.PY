
import pandas as pd
import numpy as np

# Criação de uma lista com idades
idades = [30, 42, 90, 34]
idades

# Cálculo da média das idades somando os valores e dividindo pela quantidade de elementos
sum(idades) / len(idades)

# Atribui a média à variável 'media'
media = sum(idades) / len(idades)

# Variável total inicializada com 0 para calcular a soma dos quadrados das diferenças
total = 0

# Loop para calcular a soma dos quadrados das diferenças entre a média e cada idade
for i in idades:
    total += (media - i)**2

# Cálculo da variância usando o denominador (n-1) típico para amostras
variancia = total / (len(idades) - 1)    
variancia

# Converte a lista de idades em uma Series do pandas
series_idades = pd.Series(idades)
series_idades

#%% 
# Calcula a mediana da série de idades (o valor central quando os dados são ordenados)
series_idades.median()

#%% 
# Calcula a variância usando o método var() da Series
series_idades.var()

#%% 
# Calcula a média dos valores na Series
series_idades.mean()

#%% 
# Calcula o desvio padrão dos valores na Series
series_idades.std()

#%% 
# Retorna o primeiro quartil (25%) dos valores na Series
series_idades.quantile(0.25)

#%% 
# Exibe um resumo estatístico da Series, incluindo contagem, média, desvio padrão, mínimo, máximo e quartis
series_idades.describe()

#%% 
# Retorna a forma (dimensões) da Series. No caso, (4,) pois há quatro elementos
series_idades.shape

#%% 
# Acessa o primeiro elemento da lista 'idades', que é 30
idades[0]

#%% 
# Retorna o índice da Series (posições dos elementos). Como não foi definido um índice personalizado, ele é padrão (0, 1, 2, 3)
series_idades.index      

#%%
# Acessa o primeiro elemento do índice(posição)
series_idades.index.iloc[0]  

#%%
# Acessa o primeiro elemento do índice pelo nome
series_idades.index.loc[0]  

#%% 
# Atribui um nome à Series
series_idades.name = 'idades'  
series_idades
#%% 
# Cria uma Series com nome "idades"
series_idades = pd.Series(idades, name="idades")  
series_idades

#%% 
