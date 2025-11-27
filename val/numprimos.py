def primo(num) -> bool:
    if num < 2: #Se o número for menor que 2, não é primo
        return False  
    for i in range(2, int((num ** 0.5)+ 1)):
        if num % i == 0: #Se encontrou um divisor, não é primo
            return False 
    return True  # Não encontrou divisores, então é primo


print("Números entre 1 a 100") # Auto explicativo
for i in range(1, 101):
    num = i #variavel num recebe i
    if primo(num) == True:
        print(num, 'Primo')