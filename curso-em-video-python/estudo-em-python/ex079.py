valores = []

while True:

    v = (int(input('Digite um um número: ')))
    if v not in valores:
        valores.append(v)
        print('valor adicionado')
    else:
        print('Valor ja existe, não sera adicionado. Continuando......')


    cont = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if cont == 'N':
         break

print('-='*20)
valores.sort()
print(f'Voê digitou os valores: {valores}')
