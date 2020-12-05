km = float(input('Qual é a distância da viagem em km? '))
if km <= 200 :
    print('O valor da passagem é de R${}.'.format(km*0.5))
else:
    print('O valor da passagem é de R${}.'.format(km*0.45))