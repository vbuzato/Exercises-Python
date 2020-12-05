salario = float(input('Digite o seu salário atual: R$'))

if salario > 1250:
    print('Seu novo salário será de R${:.2f}'.format(salario*1.1))
else:
    print('Seu novo salário será de R${:.2f}'.format(salario * 1.15))