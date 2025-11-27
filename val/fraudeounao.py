qtd_inicial = int(input('Insira a quantidade de produtos: '))
veridico = 0
fraude = 0

for i in range(qtd_inicial):
    preco_inicial = float(input('Insira o preço antes da promoção: '))
    preco_promocao = float(input('Insira o preço na promoção:'))

    if preco_promocao >= preco_inicial:
        fraude += 1
    
    if preco_promocao * 100 / preco_inicial < 90:
        veridico += 1

print(f'Quantidade de fraudes: {fraude}, descontos maiores que 10%: {veridico}')