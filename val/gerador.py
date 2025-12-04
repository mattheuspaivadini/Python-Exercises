import random

def gerarMatriz(linhas, colunas):
    numeros = []
    for i in range(10):
        numeros.append([0] * 10)
    return numeros

numeros = gerarMatriz(10, 10)

for i in range(10):
    for j in range(10):
        numeros[i][j] = random.randint(1, 100)
