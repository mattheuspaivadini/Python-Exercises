"""
código original ->

quantidade = 1
numero = int(input('Número: '))
maior = numero

while quantidade < 5:
    numero = int(input('Número: '))
    if numero > maior:
        maior = numero
    quantidade += 1

print(numero, maior)
"""
#Usando while True
qtd = 0
higher = 0
while True:
    num = int(input(':'))
    if num > higher:
        higher = num
    qtd += 1
    
    if qtd > 5:
        break
print(f'último valor: {num}, maior: {higher}')