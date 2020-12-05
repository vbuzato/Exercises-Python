lista = []
print(len(lista))
for x in range(0, 5):
    y = int(input('Digite um valor: '))
    if x == 0 or y > lista[-1]:
        lista.append(y)
    else:
        pos = 0
        while pos < len(lista):
            if y <= lista[pos]:
                lista.insert(pos, y)
                break
            pos +=1



print(lista)
