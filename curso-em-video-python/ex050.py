print('Soma de numeros pares')
soma = 0
cont = 0
for i in range(1, 7):
        par = int(input('digite o {}º valor: '.format(i)))
        if par % 2 == 0:
            cont += 1
            soma += par
print('A soma dos {} valores pares e:{}'.format(cont, soma))
