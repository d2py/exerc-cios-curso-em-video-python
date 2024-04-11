from random import randint
from time import sleep
valores = []
def sorteio():
    print(f'Sorteando 5 valores da lista ', end=' ')
    for c in range(1, 6):
        sort = randint(1, 10)
        valores.append(sort)
        print(sort, end=' ')
        sleep(0.3)
    print('PRONTO!')

def samopar():
    soma = 0
    for c in valores:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {valores}, temos {soma}')


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteio()
samopar()

