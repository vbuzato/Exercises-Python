altura = float(input('Digite a altura da parede(em metros): '))
largura = float(input('Digite a largura da parede(em metros): '))
mq = largura*altura
print('A parede possui {:.3f}m².'.format(mq))
print('Você precisará de {:.0f} litros de tinta para pintá-la.'.format((mq//2)+1))