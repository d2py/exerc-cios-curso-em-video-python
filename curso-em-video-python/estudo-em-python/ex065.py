sim = 'S'
cont = 0
maior = 0
menor = 0

soma = 0
media = 0
while sim == 'S':
    num = int(input('Digete o numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    sim = str(input('Quer continuar: [S/N] ')).upper().strip()
media = soma / cont
print('Voce digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O valor maior foi {} e menor foi {}.'.format(maior, menor))

