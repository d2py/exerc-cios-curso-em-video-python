
def placa(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campionato')


n = str(input('Digite o nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g) 
else:
    g = 0
if n.strip() == '':
    placa(gol=g)
else:
    placa(n, g)