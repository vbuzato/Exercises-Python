nome = input('Digite seu nome completo: ').strip()
print('Seu nome em maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome possui {} letras.'.format(len(nome) - nome.count(' '))) #conta as letras sem os espaços
print('Seu nome possui {} letras.'.format(len(nome.replace(' ','')))) #conta as letras sem os espaços - modo 2
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
nomesplit = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(nomesplit[0], len(nomesplit[0])))