from time import sleep
def analisador(* num):
    cont = maior = 0
    tot = len(num)
    print('-=' * 26)
    print('Analisando os valores passados...')
    for valor in num:
        print(valor, end=' ')
        sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' Foram informado {tot} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
analisador(2, 3, 8, 15, 6)
analisador(6, 3, 8, 1)
analisador(2,7, 3)
analisador(2,4)
analisador(0)
