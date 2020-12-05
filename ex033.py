import math
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite um último número: '))

if num1 >= num2 and num1 >= num3:
    print('O maior número é {:.2f}.'.format(num1))
elif num2 >= num1 and num2 >= num3:
    print('O maior número é {:.2f}.'.format(num2))
elif num3 >= num1 and num3 >= num2:
    print('O maior número é {:.2f}.'.format(num3))

if num1 <= num2 and num1 <= num3:
    print('O menor número é {:.2f}.'.format(num1))
elif num2 <= num1 and num2 <= num3:
    print('O menor número é {:.2f}.'.format(num2))
elif num3 <= num1 and num3 <= num2:
    print('O menor número é {:.2f}.'.format(num3))
