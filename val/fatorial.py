def fatorial(num: int) -> int:
    resultado = 1
    
    for i in range(1, num+1):
        resultado *= i
    return resultado

num = int(input('Insira o número que deseja ver o fatorial: '))

resultado = fatorial(num)

print(f'tabuada de {num} é: {resultado}')