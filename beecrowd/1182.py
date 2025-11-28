linha = int(input())
operacao = input()

soma = 0.0

#Calculo da Matriz
matriz = []
for i in range(12):
    matriz.append( [] )
    for j in range(0, 12):
        matriz[i].append(0)

#celulas da matriz
for i in range(0, 12):
    for j in range(0, 12):
        matriz[i][j] = float(input())

#soma das colunas
for i in range(0, 12):
    soma += matriz[linha][i]

#condição de soma ou média
if operacao == "S":
    print(f'{soma:.1f}')
elif operacao == "M":
    print(f'{soma/12:.1f}')