maior = 0
menor = 0
for i in range(1,6):
    peso = float(input('Digite o {}º da pssoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maoir peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))
