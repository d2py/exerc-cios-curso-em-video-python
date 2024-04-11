num = (int(input('Digite um úmero: ')),
       int(input('Digite outro úmero: ')),
       int(input('Digite mais um úmero: ')),
       int(input('Digite o ultimo número: ')))
print(f'Voce digitou os valores {num}')
print(f'o numero 9 aparesse {num.count(9)} vezes')
if 3 in num:
       print(f'O numero 3 foi digitado na {num.index(3) + 1} posição')
else:
       print('O valor 3 não foi digitado em nunhuma posição')
print('Os valores pares digitados foram: ', end='')
for c in num:
       if c % 2 == 0:
              print(c, end=' ')

