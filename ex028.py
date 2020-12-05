import random
numr = random.randrange(0,6,1,int)
num = int(input('Escolha um número entre 0 e 5: '))
if num == numr :
    print('Parabéns, você acertou!')
else:
    print('Não foi dessa vez, tente novamente.')
print('O número sorteado foi o {}'.format(numr))