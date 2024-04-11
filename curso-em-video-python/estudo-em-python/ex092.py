
from datetime import date

trabalho = dict()

trabalho['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
anoatual = date.today().year
idaatual = anoatual - anonasc
trabalho['idade'] = idaatual
trabalho['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if trabalho['ctps'] == 0:
    print('-=' * 26)
    for k, v in trabalho.items():
        print(f' - {k} tem o valor {v}.')

else:
    anocont = int(input('Ano de Contratação: '))
    apose = (35 - (anoatual - anocont)) + idaatual
    trabalho['aposentaduria'] = apose
    trabalho['salário'] = float(input('Salário: R$'))
    print('-='*26)

    for k, v in trabalho.items():
        print(f' - {k} tem o valor {v}')