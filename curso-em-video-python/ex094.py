pessoas = dict()
cadastro = list()
cprincipal = list()
soma = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))

    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).upper()

        if sexo not in 'MmFf':
            print('ERRO! Por favor, digite M ou F.')

        pessoas['sexo'] = sexo

    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']

    cadastro.append(pessoas.copy())



    res = ' '
    while res not in 'NnSs':
        res = str(input('Quer continuar? [S/N] ')).upper()

        if res not in 'NnSs':
            print('ERRO! Por favor, digite S ou N.')

    if res == 'N':
        break

print('-='*35)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastrada.')
media = soma / len(cadastro)
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulherees cadastradas foram ', end=' ')
for c in cadastro:
    if c['sexo'] == 'F':
        print(c['nome'], end=', ')
print('\nD) Lista das pessoas que estão acima da média.')
for c in cadastro:
    if c['idade'] >= media:
        print(f'    nome = {c['nome']};  sexo = {c['sexo']};  idade = {c['idade']}')
print('<< ENCERRADO >>')