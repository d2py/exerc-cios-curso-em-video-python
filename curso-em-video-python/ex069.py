tot18 = totH = totM20 = 0
while True:
    print('-' * 20)
    print('CADASTRA UMA PESSAO')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper()[0]
        if idade >= 18:
            tot18 += 1
        if sexo == 'M':
            totH += 1
        if sexo == 'F' and idade < 20:
            totM20 += 1
    continuar = ' '
    while continuar not in 'SN':
        print('-=' * 20)
        continuar = str(input('Quer continuar: [S/N]')).upper()

    if continuar == 'N':
        break
print(f'total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulher com menos de 20 anos.')