num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

resp = -1
while resp not in range(0,6):
    resp = int(input('Digite um número entre 0 e 20: '))
    if resp not in range(0,6):
        print('Tente novamente.', end=' ')

print(f'Você digitou o número {num[resp]}.')