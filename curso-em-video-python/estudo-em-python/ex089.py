matriz = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = ((nota1 + nota2) / 2)

    matriz.append([nome, [nota1, nota2], media])

    res = str(input('Quer continuar? [S/N] ')).upper()
    if 'N' in res:
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_'*26)
for i, a in enumerate(matriz):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('_'*26)

while True:

    opc = int(input('Qual nota você quer ver? [999 interrompe] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(matriz) - 1:
        print(f'Notas de {matriz[opc][0]} são {matriz[opc][1]} ')

print('<<< VOLTE SEMPRE >>>')
