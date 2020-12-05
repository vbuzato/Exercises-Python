times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná' )

print('- '*10)
print('G5'.center(20))
print('- '*10)
for c in range(0,5):
    print(f'{c+1} - {times[c]}')

print('\n')
print('- '*10)
print('Zona de Rebaixamento'.center(20))
print('- '*10)
for count in range(-4, 0):
    number = len(times) + count
    print(f'{number+1} - {times[number]}')

print('\n')
print('- '*10)
print('A-Z'.center(20))
print('- '*10)

atoz = sorted(times)
print(atoz)

n = times.index('Chapecoense')
print(f'O time da Chapecoense está na {n}ª posição.')

