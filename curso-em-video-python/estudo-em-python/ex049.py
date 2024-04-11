print('-='*12)
print('TABUADA')
print('-='*12)
tab = int(input('Digite um valor para fazer a tabuada: '))
print('-='*12)
print('Sua tabuada de {}'.format(tab))
for i in range(0, 11):
    print('{} X {} = {}'.format(tab, i, tab*i))

