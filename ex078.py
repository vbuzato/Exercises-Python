lista = []
for x in range(0, 5):
    lista.append(int(input(f'Digite um número na posição {x}: ')))

print('-='*20)
print(f'Você digitou os valores: {lista}')

maiores = []
maior = lista[0]
for i, n in enumerate(lista):
    if n > maior:
        maior = n
        maiores.clear()
        maiores.append(i)
    elif n == maior:
        maiores.append(i)

print(f'O maior valor é {maior} e ele se encontra na(s) posição(ões) {maiores}')

menores = []
menor = lista[0]
for i, n in enumerate(lista):
    if n < menor:
        menor = n
        menores.clear()
        menores.append(i)
    elif n == menor:
        maiores.append(i)

print(f'O menor valor é {menor} e ele se encontra na(s) posição(ões) {menores}')