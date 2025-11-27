while True:
    num = int(input(':'))
    if num % 2 == 0:        #Se for par, mostra a tabuada dele
        for i in range(1, (num + 1)):
            tab = num * i
            print(f'{num} X {i} = {tab}')
    else:                   #se for impar, mostra todos os números de 1 até ele
        for i in range(1, (num +1)):
            print(i)
    if num == 0:
        break
