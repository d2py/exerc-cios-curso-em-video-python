sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Adados Invalidos.Por favor, Informe seu sexo [M/F]: ')).strip().upper()
print('Sexo {} regitrado com sucesso!'.format(sexo))
