def quantidade_divisores(n:int)->int:
    div = 0
    for i in range(1, n+1):
        if n % i == 0:
            div +=1
    return div
def primo(n):
    if quantidade_divisores(n) == 2:
        return True
    else:
        return False

print('Números Primos de 1 a 100')
for n in range(1, 101):
    if primo(n) == True:
        print(n, 'Primo')