print('-='*20)
larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = alt * larg
lit_tin = area/2
print('-='*20)
print('A area da parede e {} metros quadrados. '.format(area))
print('Para pintar sera necessario {} litros de tintas.'.format(lit_tin))
