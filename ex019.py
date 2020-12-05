import random
nom1 = str(input('Digite o 1º nome: '))
nom2 = str(input('Digite o 2º nome: '))
nom3 = str(input('Digite o 3º nome: '))
nom4 = str(input('Digite o 4º nome: '))
nome = random.choice([nom1 , nom2, nom3, nom4])
print(nome)