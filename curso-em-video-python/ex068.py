from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
cont = 0
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).upper()
    print('=-' * 20)
    print(f'Voê jogou {jogador} e computador {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            print('=-' * 20)
            v += 1
        else:
            print('Você PERDEU')
            print('=-' * 20)
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU!')
            print('=-' * 20)
            v += 1
        else:
            print('Voce PERDEU')
            print('=-' * 20)
            break

    print('Vamos continuar jogando....')
    print('=-' * 20)

print(f'GAME OVER! Voce venceu {cont} vezes')