for i in range(39):
    total_vermelho = 0
    total_amarelo = 0

for j in range(10):
    vermelho = int(input('cartões vermelhos: '))
    amarelo = int(input('cartões amarelos :'))

    total_vermelho += vermelho
    total_amarelo += amarelo

print(f'Total de vermelhos: {total_vermelho}, total de amarelos: {total_amarelo}')