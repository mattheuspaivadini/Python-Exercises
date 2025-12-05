import funcao_gerador

numeros = funcao_gerador.gerarMatriz(10, 10)
#print(numeros)

funcao_gerador.preencher_matriz(numeros, 10, 20)
for i in range(len(numeros)):
    print(numeros[i])
print("//////////////////////////////////////")
distintos = funcao_gerador.valores_distintos(numeros)
print(distintos)
print(len(distintos))
print("*-" * 20)
distintos.sort()
if funcao_gerador.verificar_ordenada(distintos) == "True":
    print('Ordenada')
else:
    print('Não Ordenada')