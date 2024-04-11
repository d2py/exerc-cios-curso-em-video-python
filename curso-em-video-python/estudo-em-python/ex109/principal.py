import moeda

pr = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(pr)} é {moeda.metade(pr)}')
print(f'O dobro de {moeda.moeda(pr)} é {moeda.dobro(pr, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(pr, 10, True)}')
print(f'Desconto de 10%, temos {moeda.diminuir(pr, 10, True)}')
