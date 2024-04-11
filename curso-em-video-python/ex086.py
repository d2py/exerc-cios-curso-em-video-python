matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

'''for c in range(0, 3):
    num = int(input(f'Digite um valor para a [{0, c}]: '))
    matriz[0].append(num)
for c in range(0, 3):
    num = int(input(f'Digite um valor para a [{1, c}]: '))
    matriz[1].append(num)
for c in range(0, 3):
    num = int(input(f'Digite um valor para a [{2, c}]: '))
    matriz[2].append(num)

for p in matriz:
    print(f'[ {p[0]} ] [ {p[1]} ] [ {p[2]} ]')'''

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
    