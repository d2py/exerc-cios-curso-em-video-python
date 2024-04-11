frase = str(input('Digite uma frase: '))
palavra = frase.split()
junto = ''.join(palavra)
inverso = ('')
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')