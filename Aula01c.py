n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} é: {}'.format(n1, n2, s))
print('Tipo: ',type(s))
print(s.is_integer())

algo = input('Digite algo:')
print(algo.isnumeric())

#=================================

nome = str(input('Qual é seu nome? '))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('Prazer em te conhecer {:+>20}!'.format(nome))

