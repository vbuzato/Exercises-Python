num = int(input('Digite um número: '))
x = 0
count = num
resultado = num
while True:
    if count != 0:
        count -= 1
        if count == 1 or num == 1:
            break
        resultado = resultado * count

print(f'O fatorial de {num} é {resultado}')