import random

numeros = []
for i in range(10):
    numeros.append([0] * 10)

for i in range(10):
    for j in range(10):
        numeros[i][j] = random.randint(1, 100)
