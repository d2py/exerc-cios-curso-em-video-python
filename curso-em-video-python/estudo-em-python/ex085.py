
lista = [[], []]

for c in range(1, 8):
    numero = (int(input(f'Digite o {c}º numero: ')))

    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)


print('-='*20)
lista[0].sort()
lista[1].sort()
print(f'Os volores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
