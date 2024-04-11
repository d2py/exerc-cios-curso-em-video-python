from time import sleep
opcao = 0
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

while opcao != 5:
    print( '''
    ESCOLHA UMA OPÇÂO
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')

    opcao = int(input('>>>Digite a opção: '))

    if opcao == 1:
        soma = num1 + num2
        print('A Soma dos valor {}'.format(soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação dos valores {}'.format(mult))
    elif opcao == 3:
        if num1 > num2:
            print('Primeiro valor e maior {} que o segundo valor {}'.format(num1, num2))
        else:
            print('O segundo valor e maior {} que o primeiro valor {}'.format(num2, num1))
    elif opcao == 4:
        print('Digite novos valores')
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('Sanindo do programa....')
    print('-=-' * 15)
    sleep(3)
print('Fim do Programa, Volte Sempre')
