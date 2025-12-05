import random

def gerarMatriz(qtd_linhas:int, qtd_colunas:int, valor=0)->list:
    matriz = []
    for i in range(qtd_linhas):
        matriz.append([valor] * qtd_colunas)
    return matriz

def preencher_matriz(matriz:list, menor=1, maior=100):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            numeros[i][j] = random.randint(menor, maior)

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
        else:
            return True

numeros = gerarMatriz(10, 10)
#print(numeros)

preencher_matriz(numeros, 10, 20)
print(numeros)

print("//////////////////////////////////////")
distintos = valores_distintos(numeros)
print(distintos)
print(len(distintos))
print("*-" * 20)
ordenada = verificar_ordenada(distintos)
if ordenada == "True":
    print('Ordenada')
else:
    print('Não Ordenada')