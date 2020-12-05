from math import sqrt, pow
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#hip = sqrt((co**2)+(ca**2))
hip = sqrt(pow(co,2)+pow(ca,2))
print('O valor da hipotenusa é: {:.2f}.'.format(hip))