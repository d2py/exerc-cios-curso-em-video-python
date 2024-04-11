import moeda

pr = float(input('Digite o preço: R$'))
print(f'A metade de {pr} é {moeda.metade(pr)}')
print(f'O dobro de R${pr} é R${moeda.dobro(pr)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(pr, 10)}')
print(f'Desconto de 10%, temos R${moeda.diminuir(pr, 10)}')