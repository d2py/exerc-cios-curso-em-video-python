maior = 0
menor = 0
cont = 0
posMa = list()
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]

        if valores[c] < menor:
            menor = valores[c]


print('-='*20)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na posições ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}...', end='')
print(f'\nO menor valor digitado foi {menor} na posições ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}...', end='')
print('-='*20)
print()