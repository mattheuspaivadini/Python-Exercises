
def gerarMatriz(qtd_linhas:int, qtd_colunas:int, valor=0)->list:
    matriz = []
    for i in range(qtd_linhas):
        matriz.append([valor] * qtd_colunas)
    return matriz

def preencher_matriz(matriz:list, menor=1, maior=100):
    import random
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = random.randint(menor, maior)

def valores_distintos(matriz: list) -> list:
    valor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] not in valor:
                valor.append(matriz[i][j])
    return valor

def verificar_ordenada(vetor: list)->bool:
    for i in range(len(vetor)-1):
        if (vetor[i] > vetor[i+1]):
            return False
    return True