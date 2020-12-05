n = 1
while n > -1:
    n = int(input('----------------------------------\nQuer ver a tabuada de qual número? \n----------------------------------'))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')