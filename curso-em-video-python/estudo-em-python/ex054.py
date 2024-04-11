from datetime import date
atual = date.today().year
contm = 0
contm1 = 0
for i in range(1, 8):
    ano = int(input('Digite o {}º ano: '.format(i)))
    ida = atual - ano
    if ida < 18:
        contm += 1
    else:
        contm1 += 1
print('Temos {} pessoas que são menores de 18 anos'.format(contm))
print('Temos {} pessoas que ja são maiores de 18 anos'.format(contm1))