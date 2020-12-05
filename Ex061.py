termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

x = 1
while x != 0:
    n = int(input('Quantos termos você quer ver? '))
    if n == 0:
        exit()
    for c in range(0, n):
        print(termo)
        termo = termo + razao





