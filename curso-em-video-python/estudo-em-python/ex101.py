'''def par(n=1):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')'''

def votar(ano):
    from datetime import date
    anoataul = date.today().year
    idade = anoataul - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(votar(nasc))
