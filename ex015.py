km = float(input('Digite a kilometragem rodada: '))
dias = int(input('Digite a quantidade de dias utilizados: '))
valorkm = km * 0.15
valordias = dias * 60
total = valordias + valorkm
print('O valor total é de: R${:.2f}'.format(total))