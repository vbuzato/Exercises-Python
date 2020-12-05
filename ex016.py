from math import floor, ceil
num = float(input('Digite um número: '))
print('O número {:.2f} tem a parte inteira {}.'.format(num, floor(num)))
print('O número {:.3f} arredondado para cima é {}.'.format(num,ceil(num)))

# O comando floor arredonda para baixo
# O comando ceil arredonda para cima