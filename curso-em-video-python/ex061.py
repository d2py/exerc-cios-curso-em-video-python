c = 1
pt = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a Razão: '))
ter = pt
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(ter), end='')
        ter += raz
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais ?'))
print('FIM')
