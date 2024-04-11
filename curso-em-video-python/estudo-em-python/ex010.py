real = float(input('Quantos voce tem na carteira?: '))

dolar = real / 3.27

print('-='*20)
print('Com R$ {:.2f} voce pode comprar $$ {:.2f} dolar '.format(real, dolar))
