from random import randint

derrota = False
nvit = 0
while derrota == False:
    valor = int(input('Digite um valor: '))
    decisao = ''
    while decisao != 'P' and decisao != 'I':
        decisao = str(input('Você prefere PAR ou ÍMPAR? [P/I] ')).upper()

    rand = randint(0,10)
    result = rand + valor

    if result % 2 == 0:
        if decisao == 'P' :
            print('Você venceu! Vamos jogar novamente!\n\n')
            nvit += 1
        else:
            print('Você perdeu.\n\nJogo encerrado!')
            derrota = True
    else:
        if decisao != 'P' :
            print('Você venceu! Vamos jogar novamente!\n\n')
            nvit += 1
        else:
            print('Você perdeu.\n\nJogo encerrado!')
            derrota = True

print(f'Você venceu {nvit} vezes.')