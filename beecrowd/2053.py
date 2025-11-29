matriz = []
maiores_toques = 0

for i in range(8):
    matriz.append([0] * 4)

for j in range(20):
    L, C = map(int, input().split())
    matriz[L][C] += 1
    if matriz[L][C] > maiores_toques:
        maiores_toques = matriz[L][C]

for k in range(8):
    for m in range(4):
        if matriz[k][m] == maiores_toques:
            print(f'{m} {k}')