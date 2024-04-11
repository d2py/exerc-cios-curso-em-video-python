listTime = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',  'Flamengo',
            'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Athlético-PR', 'Bahia',
            'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('='*30)
print(f'Lista de times do Brasileirão {listTime}')
print('='*30)
print(f'OS 05 primeiros são {listTime[:5]}')
print('='*30)
print(f'Os 4 últimos são {listTime[-4:]}')
print('='*30)
print(f'Times em ordem alfabética: {sorted(listTime)}')
print('='*30)
print(f'O time Chapecoense esta na {listTime.index('Chapecoense') + 1}º posição')
