nome = []
idade = []
sexo = []

nome = ['Joana', 'Vinicius', 'Lucas','Junior','Maria','Pri']
idade = [80, 32, 56, 16, 12, 19]
sexo = ['Mulher','Homem','Homem','Homem','Mulher','Mulher']

somaIdade = 0
for c in range(0, len(idade)):
    somaIdade += idade[c]
print('A média das idades é: {:.2f}'.format(somaIdade / len(idade)))

mv = 0
for c in range(0, len(idade)):
    if sexo[c] == 'Homem' and idade[c] >= mv:
        mv = idade[c]

for c in range(0, len(idade)):
    if sexo[c] == 'Homem' and idade[c] == mv:
            print('Mais velho(s): {}, com {} anos.'.format(nome[c], mv))

x = 0
for c in range(0, len(idade)):
    if sexo[c] == 'Mulher':
        if idade[c]<21:
            x = x + 1

print('{} mulheres tem menos que 21 anos.'.format(x))




