from random import randint
from time import sleep
matriz = []

print('-'*30)
print('JOGO DA MEGA SENA'.center(30))
print('-'*30)
sorteio = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {sorteio} JOGOS -=-=-= ')

for jogo in range(1, sorteio+1):
    print(f'Jogo {jogo}: ', end='')
    matriz.clear()
    for c in range(1, 7):
       sorteado = randint(1, 60)
       if sorteado in matriz:
           sorteado = randint(0, 60)
           matriz.append(sorteado)
       else:
           matriz.append(sorteado)
    matriz.sort()
    print(matriz)
    sleep(1)
print('-=-=-=-= < BOA SORTE! > -=-=-=-=')
