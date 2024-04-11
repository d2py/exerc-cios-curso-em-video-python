extenso = ('Zero','Um', 'Does', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez','Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove','Vinte')

#numero = int(input('Digite um numero entre 0 e 20: '))

#while numero < 0 or numero > 20:
#    numero = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
#for pos, ext in enumerate(extenso):
#    if numero == pos:
#        print(f'Voce digitou o numero {ext}:')


while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novanmente', end='')
print(f'Vove digitou o numero {extenso[numero]}')