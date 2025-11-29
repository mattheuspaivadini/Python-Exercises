operacao = input()
matriz = []
soma = 0.0
cont = 0

#Calculo da Matriz
for i in range(12):
    linha = []
    for j in range(0, 12):
        linha.append(float(input()))
    matriz.append(linha)

for i in range(12):
    for j in range(12):
        if j > i:
            soma += matriz[i][j]
            cont += 1

#condição de soma ou média
if operacao == "S":
    print(f'{soma:.1f}')
elif operacao == "M":
    print(f'{soma/cont:.1f}')