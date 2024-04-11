'''galera = list()
dado = list()
totmai = totmen = 0
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] > 20:
        print(f'{p[0]} e maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')'''


pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()

    res = str(input('Quer continuar[S/N]: ')).upper()
    if res in 'Nn':
        break

print('-='*30)
print(f'Ao todo, você digitou {len(pessoas)} pessoas.')
print(f'O menor peso foi de {menor} kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
print(f'O maior peso foi de {maior} KG. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f' [{p[0]}]', end='')
print()
print('-='*30)
