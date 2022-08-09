from math import sqrt
import numpy as np

"""
Objetivo: calcular o grau de dispersão de um conjunto de valores em torno da média.

- Amplitude: diferença entre o maior e o menor valor de um conjunto de dados.
- Desvio médio: diferença entre o valor e a média
- Variância: mensura o grau de dispersão de um conjunto de valores em torno da média.
- Desvio padrão: raiz quadrada da variância.
"""

a = [5, 8, 10, 12, 15]
variancia_A = np.var(a)
print(variancia_A)
desviopadrao_A = sqrt(variancia_A)
print(desviopadrao_A)
