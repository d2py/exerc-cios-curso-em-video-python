from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opcão de listar o conteudo de um arquivo!
        lerArquivo(arq)

    elif resposta == 2:
        # Função de cadastrar nova pessoa
        cabecalho('NOVO CADATRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Ate logo!')
        print(linha())
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)



