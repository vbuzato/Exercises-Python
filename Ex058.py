import random
numr = random.randrange(0,6,1,int)
x = 1
while numr != int(input('Escolha um número entre 0 e 5: ')):
    x += 1

print('Parabéns! Você precisou de {} tentativas para vencer.'.format(x))
