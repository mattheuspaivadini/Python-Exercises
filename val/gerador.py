import random

def gerarMatriz(qtd_linhas:int, qtd_colunas:int, valor)->list:
    matriz = []
    for i in range(qtd_linhas):
        matriz.append([valor] * qtd_colunas)
    return matriz

def preencher_matriz(matriz:list, menor=1, maior=100):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            numeros[i][j] = random.randint(menor, maior)

numeros = gerarMatriz(10, 10, 4)
preencherMatriz = preencher_matriz(numeros)
print(numeros)