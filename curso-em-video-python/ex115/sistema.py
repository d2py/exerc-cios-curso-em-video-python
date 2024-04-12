from lib.interface import *
from time import sleep


while True:
    resposta = menu(['Criar Arquivo', 'Cadatrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('Opcao 1')
    elif resposta == 2:
        print('Opcao 2')
    elif resposta == 3:
        print('Saindo do sistema... Ate logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)