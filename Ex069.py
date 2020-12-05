idades = []
sexos = []
while True:
    print('--------------------------------')
    print('Cadastre uma Pessoa')
    print('--------------------------------')

    idades.append(int(input('Idade: ')))

    sexo = 'a'
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    sexos.append(sexo)

    print('--------------------------------')
    print('Pessoa cadastrada com sucesso!')
    decisao = 'A'
    while decisao not in 'SN':
        decisao = str(input('Você deseja cadastrar mais alguém? [S/N] ')).upper()
    print('--------------------------------')

    if decisao == 'N':
        break


count = 0
for c in range(0, len(idades)):
    if idades[c] >= 18:
        count += 1
print(f'{count} pessoas tem mais que 18 anos.')

count = 0
for c in range(0, len(idades)):
    if sexos[c] == 'M':
        count += 1
print(f'{count} pessoas são homens.')

count = 0
for c in range(0, len(idades)):
    if sexos[c] == 'F' and idades[c] < 20:
        count += 1
print(f'{count} pessoas são mulheres com menos de 20 anos.')