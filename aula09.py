frase = 'Curso em Vídeo Python'
print(frase[9])
print(frase[9:14])
print(frase[0:21:2]) #Pula a cada 2 caracteres
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o')) #Conta quantas letras 'o' tem a string
print(frase.count('o', 0, 13)) #Conta quantas letras 'o' tem do inicio ate o caracter 12 da string
print(frase.find('deo'))  #Retorna a posição que se encontra o inicio da string procurada
print(frase.find('texto')) #Quando não encontrar um string semelhante, retorna o valor -1
print('Curso' in frase) #Retona um valor booleano
print(frase.replace('Curso', 'Aula'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())