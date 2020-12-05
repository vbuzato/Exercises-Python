nome = input('Digite seu nome: ')
nome = nome.split()
cont = nome.count('Silva')
if cont >= 1:
    print('O seu nome contém Silva.')
else:
    print('O seu nome não contém Silva.')