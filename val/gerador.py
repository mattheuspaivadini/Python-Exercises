import random

def gerarMatriz(qtd_linhas:int, qtd_colunas:int)->list:
    matriz = []
    for i in range(qtd_linhas):
        matriz.append([0] * qtd_colunas)
    return matriz

numeros = gerarMatriz(10, 10)

for i in range(10):
    for j in range(10):
        numeros[i][j] = random.randint(1, 100)