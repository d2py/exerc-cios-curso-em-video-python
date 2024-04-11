cont = soma = 0
numero = int(input('Digite um numero [999 para parar]: '))
while numero != 999:
        cont += 1
        soma += numero
        numero = int(input('Digite um numero [999 para parar]: '))
print('Você digitol  {} NÚMEROS e a SOMA deles e {}.'.format(cont, soma))
