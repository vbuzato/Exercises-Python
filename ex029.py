import random
vel = random.randrange(60,140,1,int)
print('A velocidade foi de {} Km/h.'.format(vel))
if vel > 80 :
    print('Você foi multado em R${:.2f}.'.format((vel-80)*7))