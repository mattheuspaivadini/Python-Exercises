N = int(input())

for i in range(N):
    X, Y, Z = map(float, input().split())
    RESULTADO = (X * 2 + Y * 3 + Z * 5) / 10
    print(f'{RESULTADO:.1f}')