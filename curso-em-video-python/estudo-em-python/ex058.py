

from random import randint
from time import sleep
'''computador = 0
jogador = 1
cont = 0
computador = randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

while jogador != computador:
    jogador = int(input('Qual seu palpite? '))
    print('PROCESSANDO...')
    sleep(3)


    cont += 1

    if jogador == computador:
        print('PARABENS! Voce conseguiu me vencer!')
        print('Porem você fez {} tentaivas para ganhar'.format(cont))
    else:

        print('GAMNHEI! Eu pensei no numero {} e não no {}'.format(computador, jogador))'''


computador = randint(0, 10)
print('Sou seu computador.... Acabei de pensar em um numero entre 0 e 10.')
print('Será que voce consegui adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabens!'.format(palpites))
