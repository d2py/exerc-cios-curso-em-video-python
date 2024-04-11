"""produtos = ('Lapis...........R$ 1.75',
            'Borracha........R$ 2.00',
            'Caderno.........R$ 10.85',
            'Estojo..........R$ 6.96',
            'Caneta..........R$ 1.20',
            'Lapis Cor.......R$ 9.30')
print('='*25)
print('{:^25}'.format('TABELA DE PREÇO'))
print('='*25)
for c in produtos:
     print(c)
print('='*25)"""

produtos = ('Lapis', 1.75,
            'Borracha', 2.00,
            'Caderno', 10.58,
            'Estojo', 6.96,
            'Caneta', 1.20,
            'Lapis', 9.30)

print('='*40)
print(f'{"TABELA DE PREÇO":^40}')
print('='*40)
for pos in range(0, len(produtos)):
     if pos % 2 == 0:
         print(f'{produtos[pos]:.<30}', end='')
     else:
         print(f'R${produtos[pos]:>8.2f}')
print('='*40)