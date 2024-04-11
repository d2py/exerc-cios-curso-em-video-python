sal = float(input('Digite o salrio do funcionario: '))

alm = (sal * 15/100)
nov_sal = sal + alm
print('-='*20)
print('O almento foi de R$ {:.2f}'.format(alm))
print('Novo salario com 15% de almento e de R$ {:.2f}'.format(nov_sal))
