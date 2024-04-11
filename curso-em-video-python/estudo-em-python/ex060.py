fatorial = 1
valor = int(input('Digite um valor para encontra o fatorial: '))
print('Calculando {}! = '.format(valor), end='')
while valor >= 1:
    print('{}'.format(valor), end='')
    print(' x ' if valor > 1 else ' = ', end='')
    fatorial *= valor
    valor -= 1
print('{}'.format(fatorial))
