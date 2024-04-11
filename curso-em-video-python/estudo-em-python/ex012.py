prec = float(input('Digite o valor do produto: '))

desc = prec - (prec * 5 / 100)

print('O novo preço com desconto de 5% e de R$ {:.2f}'.format(desc))
