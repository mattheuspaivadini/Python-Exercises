while True:
    num = int(input('Digite um número: '))
    for i in range(1, num+1):
        tab = num * i
        print(f'{num} X {i} = {tab}')