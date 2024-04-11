lista = []
listPar = []
listImp = []

while True:

    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        listPar.append(num)
    else:
        listImp.append(num)

    res = str(input('Quer continuar [S/N]: ')).upper()
    if res in 'Nn':
        break
print('-='*25)
print(f'A lista digitada foi {lista}.')
print(f'A lista com os valores Impares e {listImp}.')
print(f'A lista com os valores Pares e {listPar}.')
print('-='*25)