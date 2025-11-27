def quadrant(x, y: int) -> str:
    if x > 0 and y > 0:
        return 'primeiro'
    elif x > 0 and y < 0:
        return 'quarto'
    elif x < 0 and y < 0:
        return 'terceiro'
    elif x < 0 and y > 0:
        return 'segundo'
    elif x == 0 or y == 0:
        return None
    

while True:
    x, y = map(int, input().split())
    
    resposta = quadrant(x, y)

    if resposta == None:
        break
    else:
        print(resposta)
