n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
x = 0
while x != 1 and x != 2 and x != 3:
    x = int(input('O que vc deseja fazer?\n|1| - SOMAR\n|2| - MULTIPLICAR\n|3| - SAIR DO PROGRAMA\n'))
    if x == 1:
        print('Resultado: {}'.format(n1 + n2))
        x=0
    elif x == 2:
        print('Resultado: {}'.format(n1 * n2))
        x=0

