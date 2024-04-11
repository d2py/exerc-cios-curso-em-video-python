import moeda

pr = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(pr)} é {moeda.moeda(moeda.metade(pr))}')
print(f'O dobro de {moeda.moeda(pr)} é {moeda.moeda(moeda.dobro(pr))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(pr, 10))}')
print(f'Desconto de 10%, temos {moeda.moeda(moeda.diminuir(pr, 10))}')