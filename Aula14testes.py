from random import randint
from time import sleep

computador = randint(0, 2)
escolha = ("Pedra", 'Papel', 'Tesoura')
print("-=" * 20)
print('BEM VINDO AO JOGO DE JOKENPO !!!')
print("-=" * 20)
print("Opcoes:\n[0] Pedra\n[1] Papel\n[2] Tesoura")
jogador = int(input("Digite sua opcao: "))
print("")
print("JOOOO")
sleep(1)
print("KEEEEN")
sleep(1)
print("POOOO !!!")
print("-=" * 20)
print("Computador jogou {} e voce jogou {}".format(escolha[computador], escolha[jogador]))
print("-=" * 20)

if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("VOCE VENCEU !!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU !!")
    else:
        print("Jogada invalida")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCEU !!")
    elif jogador == 1:
        print("EMPATE!!")
    elif jogador == 2:
        print("JOGADOR VENCEU !!")
    else:
        print("Jogada invalida")
elif computador == 2:
    if jogador == 0:
        print("VOCE VENCEU!!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU !!")
    elif jogador == 2:
        print("EMPATE!!")
    else:
        print("Jogada invalida.")
else:
    print("Opcao invalida!!")


