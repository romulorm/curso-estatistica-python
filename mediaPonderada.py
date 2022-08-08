import numpy as np

""" Exemplo: Notas de um aluno nas provas do ENEM, onde os pesos 
das matérias são diferentes """

notas = [718.91, 521.33, 627.9, 610.12, 930]
pesos = [5, 2, 2, 4, 5]

""" mediapond = 718,91 x 5 + 521.33 x 2 + .../18 """

mediapond = np.average(notas, weights=pesos)

print(mediapond)