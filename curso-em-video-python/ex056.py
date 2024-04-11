maioridadehomem = 0
somaidade = 0
mediaidade = 0
nomevelho = ''
totmulher20 = 0
for cad in range(1,5):
    print('----- {}º PESSOA -----'.format(cad))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]')).strip()
    somaidade += idade
    if cad == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / cad
print('A média de idade do grupo é de {:.2f}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos!'.format(totmulher20))