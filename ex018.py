import math

num = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O Cosseno de {} é: {:.2f}.\nO Seno de {} é: {:.2f}.\nA Tangente de {} é: {:.2f}.'.format(num,cos,num,sen,num,tan))
