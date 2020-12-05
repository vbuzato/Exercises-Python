frase = input('Digite uma frase: ')
cont = frase.count('a')
print('A letra "a" apareceu {} vezes.'.format(cont))
fp = frase.find('a')
lp = frase.rfind('a')
print('A letra "a" apareceu pela primeira vez no espaço {}.'.format(fp)) #fp = first position
print('A letra "a" apareceu pela última vez no espaço {}.'.format(lp)) #lp = Last position
