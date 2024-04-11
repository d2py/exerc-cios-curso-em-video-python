
lista = []
while True:

    cont = 0
    lista.append(int(input('Digite um valor: ')))
    lista.sort(reverse=True)


    res = str(input('Quer continuar?[N/S]: ')).upper()
    if res == 'Nn':
        break

print('-='*25)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista!.')
else:
    print('O valor 5 não faz parte da lista!.')
print('-='*25)