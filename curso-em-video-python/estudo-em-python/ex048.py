print('A soma de imapres multiplos de 3.')
soma = 0
cont = 0
for i in range(1, 501,2):
    if i % 3 ==0:
        
        cont += 1
        soma += i
print('A soma de todos os {} valores solicitados foram: {}'.format(cont, soma))
