gasto = 0
tot1000 = 0
tot = 0
pro = ''
menor = 0
while True:

    produto = str(input('Nome do produto: '))

    preco = float(input('Preço:R$ '))

    gasto += preco
    tot += 1

    if preco > 1000:
        tot1000 += 1

    if tot == 1 or preco < menor:
        menor = preco
        pro = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N:] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A soma da compra e R${gasto:.2f}.')
print(f'No total tem {tot1000} com valor a cima de R$1000 resis.')
print(f'O produto mais barato custa {menor} e o nome do produto e {pro}.')