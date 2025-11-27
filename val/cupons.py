def quantidade_cupons(valor_compra: float) -> int:
    cupons_calculados = int(valor_compra // 50)
    return cupons_calculados

cupons_estoque = 100
clientes_beneficiados = 0
cupons_faltantes = 0

while cupons_estoque > 0:
    valor_compra = float(input('Insira o valor de sua compra: '))
    cupons_esperados = quantidade_cupons(valor_compra)
    
    if valor_compra < 50:
        print('Valor insuficiente para um cupom (valor mínimo: R$ 50,00)')

    if cupons_estoque >= cupons_esperados:
        clientes_beneficiados += 1
        cupons_estoque -= cupons_esperados
    else:
        clientes_beneficiados += 1
        cupons_entregues = cupons_estoque
        cupons_faltantes = cupons_esperados - cupons_entregues
        cupons_estoque = 0
        break
print(f'Clientes beneficiados: {clientes_beneficiados}\nQuantidade de cupons faltantes para o último cliente: {cupons_faltantes}')

