valores = []
valores.append(4)
valores.append(3)
valores.append(9)

for x in valores:
    print(f'{x}...', end='')

print('\n .................................. \n\n')

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor: {v}')

print('\n .................................. \n\n')

novalista = list()
for x in range(0,3):
    novalista.append(int(input('Digite um número:')))
for c, v in enumerate(novalista):
    print(f'Na posição {c}, encontrei o valor: {v}')