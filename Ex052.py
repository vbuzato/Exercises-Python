n = int(input('Digite um número: '))

for c in range(1, n):
    if n == 1:
        print('{} é um número primo.'.format(n))
    elif n%c == 0:
        print('{}  não é um número primo.'.format(n))
    else:
        print('{} é um número primo.'.format(n))
