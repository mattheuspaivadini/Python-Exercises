times = int(input())
the_times = 0

while True:
    X, Y = map(int, input().split())
    the_times = the_times + 1

    if Y == 0:
        print('divisao impossivel')
    else:
        print(f'{X / Y:.1f}')
    if the_times == times:
        break