import random #Por que sempre aleatório?

maior_valor = 0
contador = 0
while True:
    num = random.randint(10, 50)

    if num > maior_valor:
        maior_valor = num
    contador += 1 #Isso não foi pedido, mas resolvi colocar pq eu quis
    if num == 10 or num == 50:
        break
print(f'{num} e maior valor: {maior_valor} e levou {contador} vezes')