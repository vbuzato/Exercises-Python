from time import sleep

print('Contagem regressiva de 10 segundos para a virada:')
for n in range(10, 0, -1):
    print(n)
    sleep(1)

print('Feliz Ano Novo')