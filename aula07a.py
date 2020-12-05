#Equação de segundo grau

a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
s = a + b
m = a * b
d = a / b
di = a//b
e = a**b
print('A soma é {}, \nO produto é {} e a divisão é {}'.format( s, m, d), end=' ' )
print('Divisão inteira é {} e potência é {}'.format(di, e), end='===')