N = int(input())
SAPOS = 0
COELHOS = 0
RATOS = 0

for i in range(N):
    QTD, LETRA = input().split()
    str(LETRA)

    if (LETRA == 'C'):
        COELHOS = COELHOS + int(QTD)
    if (LETRA == 'R'):
        RATOS = RATOS + int(QTD)
    if (LETRA == 'S'):
        SAPOS = SAPOS + int(QTD)
    
#variaveis finais
TOTAL = COELHOS + RATOS + SAPOS
POR_COELHOS = (COELHOS / TOTAL) * 100
POR_RATOS = (RATOS / TOTAL) * 100
POR_SAPOS = (SAPOS / TOTAL) * 100

#prints
print(f'Total: {TOTAL} cobaias')
print(f'Total de coelhos: {COELHOS}')
print(f'Total de ratos: {RATOS}')
print(f'Total de sapos: {SAPOS}')
print(f'Percentual de coelhos: {POR_COELHOS:.2f} %')
print(f'Percentual de ratos: {POR_RATOS:.2f} %')
print(f'percentual de sapos: {POR_SAPOS:.2f} %')