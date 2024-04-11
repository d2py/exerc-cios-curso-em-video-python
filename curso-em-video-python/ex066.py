cont = soma = 0
while True:
    numero = int(input('Digite um valor [999 Para parar]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Você digitou {cont} números e a soma deles e {soma}.')
