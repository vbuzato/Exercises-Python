
n = []
for c in range(1, 7):
    n.insert(c,int(input('Digite o {}º numero: '.format(c))))

count = len(n)
soma = 0
for c in range(0, count):
    if n[c] % 2 == 0:
        soma = soma + n[c]

print(soma)