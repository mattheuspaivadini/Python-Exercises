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

# tanto esse quanto o anterior fazem as mesmas coisas, o que muda é so os comandos
higher = 0
for i in range(1, 6):
    num = int(input(':'))

    if num > higher:
        higher = num

print(f'Last number: {num}, higher number: {higher}')