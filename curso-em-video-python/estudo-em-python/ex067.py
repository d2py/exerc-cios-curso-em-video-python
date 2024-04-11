cont = 1

while True:
    numero = int(input('Quer ver a tabuada de qual valor?: '))
    print('-'*30)
    if numero < 0:
        break
    for cont in range(1, 11):
        print(f'{cont} X {numero} = {numero * cont}')
    print('#' * 30)
print('PROGRAMA ENCERRADO. Volte sempre')
