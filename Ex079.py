lista = list()
resp = 'S'
while resp != 'N':
    valor = int(input('Digite um número: '))
    if valor in lista:
        print('Este número já existe.')
    else:
        lista.append(valor)
    resp = input('Deseja continuar? (S/N) ').upper()

print('=-'*20)
print(f'Você digitou os valores: {lista}')