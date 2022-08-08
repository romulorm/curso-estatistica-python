import numpy as np


"""
Mediana divide o conjunto de dados em duas partes iguais,
 onde é preciso ordenar o conjunto de dados.
 """

"""
 Regra:
 Conjunto ímpar: a mediana será o valor central
 Conjunto par: a mediana será a média aritimética dos valores
  centrais.
  """

conjunto_A = [87, 13, 11, 10, 10]
conjunto_B = [23, 31, 17, 18]

"""
a_reord = {10, 10, 11, 13, 87}
mediana(a) = 11

b_reord = {17, 18, 23, 31}
mediana(b) = 18 + 23 / 2 = 20.5
"""

mediana_A = np.median(conjunto_A)
media_A = np.mean(conjunto_A)
print(f'Mediana_A: {mediana_A}')
print(f'Média_A: {media_A}')

mediana_B = np.median(conjunto_B)
media_B = np.mean(conjunto_B)
print(f'Mediana_B: {mediana_B}')
print(f'Média_B: {media_B}')