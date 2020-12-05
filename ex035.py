r1 = float(input('Digite o tamanho da reta 1: '))
r2 = float(input('Digite o tamanho da reta 2: '))
r3 = float(input('Digite o tamanho da reta 3: '))

x = False
if abs(r3-r2) < r1 and r1 < (r3+r2):
    if abs(r3-r1) < r2 and r2 < (r3+r1):
        if abs(r2-r1) < r3 and r3 < (r2+r1):
            x = True

print('Estas retas formam um triângulo.' if x == True else 'Estas retas não formam um triângulo.')

'''if x == True:
    print('Estas retas formam um triângulo.')
else:
    print('Estas retas não formam um triângulo.')
'''


'''
if abs(r3-r2) < r1 and r1 < (r3+r2):
    if abs(r3-r1) < r2 and r2 < (r3+r1):
        if abs(r2-r1) < r3 and r3 < (r2+r1):
            print('Estas retas formam um triângulo.')
        else:
            print('Estas retas NÃO formam um triangulo.')
    else:
        print('Estas retas NÃO formam um triangulo.')
else:
    print('Estas retas NÃO formam um triangulo.')
'''