import random
num = round(random.random()*100, 0)
if num % 2 == 0 :
    print('O número {:.0f} é PAR.'.format(num))
else:
    print('O número {:.0f} é ÍMPAR.'.format(num))