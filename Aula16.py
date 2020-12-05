lanche = ('Hambúerguer', 'Suco', 'Pizza', 'Pudim')

# 1ª forma de fazer
for comida in lanche:
    if comida == 'Suco':
        print(f'Eu vou beber {comida}!')
    else:
        print(f'Eu vou comer {comida}!')

# 2ª forma de fazer
for pos, comida in enumerate(lanche):
    if comida == 'Suco':
        print(f'Eu vou beber {comida}! Posição {pos}.')
    else:
        print(f'Eu vou comer {comida}! Posição {pos}.')

# 3ª forma de fazer
for comida in range(0, len(lanche)):
    if lanche[comida] == 'Suco':
        print(f'Eu vou beber {lanche[comida]}! Posição {comida}.')
    else:
        print(f'Eu vou comer {lanche[comida]}! Posição {comida}.')