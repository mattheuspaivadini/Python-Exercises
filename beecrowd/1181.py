indice = int(input())
operacao = input()

matriz = []
soma = 0.0

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

for k in matriz[indice]:
    soma += k

if operacao == "S":
    print(f'{soma:.1f}')
elif operacao == "M":
    print(f'{soma/12:.1f}')