import statistics as st

"""
Moda: valor com mais frequência em um conjunto de dados.
Pode ser unimodal, bimodal, multimodal ou amodal (sem moda).
"""

a = [11, 2, 2, 9, 7]
b = [4, 4, 19]
c = [3, 3, 1, 9, 9]

moda_A = st.mode(a)
moda_B = st.mode(b)
moda_C = st.multimode(c)
print(moda_A)
print(moda_B)
print(moda_C)