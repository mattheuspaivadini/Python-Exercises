#criar matriz
matriz = []
for i in range(4):
    matriz.append([0] * 6)

#input bombas

for k in range(int(input())):
    L, C = map(int, input().split())
    matriz[L-1][C-1] = 'B'

#escanner tabu
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if matriz[i][j] == 'B':
            for delta_i in [-1, 0, 1]:
                for delta_j in [-1, 0, 1]:
                    nova_linha, nova_coluna = i + delta_i, j + delta_j
                    if 0 <= nova_linha < 4 and 0 <= nova_coluna < 6 and matriz[nova_linha][nova_coluna] != 'B':
                        matriz[nova_linha][nova_coluna] += 1

#print tela
passar = input().split()
L_passar = int(passar[0])
C_passar = int(passar[1])
if matriz[L_passar-1][C_passar-1] == 0:
    print('X')
else:
    print(matriz[L_passar-1][C_passar-1])