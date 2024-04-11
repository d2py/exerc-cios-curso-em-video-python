jogo = dict()
golm = list()
somagol = 0
jogo['nome'] = str(input('Nome do jogador: '))
quatj = int(input(f'Quantas partidas {jogo["nome"]} jogou? '))
for c in range(0, quatj):
    golm.append(int(input(f'  Quantos gols na partida {c}? ')))



jogo['gols'] = golm[:]
jogo['total'] = sum(golm)
print('-='*35)
print(f'{jogo}')
print('-='*35)
print(f'O jogador {jogo["nome"]} jogou {len(jogo["gols"])} partidas')
for k, v in jogo.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*35)

for c, v in enumerate(golm):
    print(f'  => Na partida {c}, fez {v}')
print(f'Foi um total de {jogo["total"]} gols')