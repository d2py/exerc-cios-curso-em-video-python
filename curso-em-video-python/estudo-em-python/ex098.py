from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')


    if i < f:
        for c in range(i, f, p):
            print(c,end=' ')
            sleep(1)
        print('FIM')
        print('=' * 35)
        sleep(1.3)
    if i > f:
        for c in range(i, f, -p):
            print(c,end=' ')
            sleep(1)
        print()



# Programa principal
contador(1,10,1)
contador(10,1,2)
print('=' * 35)
print('Agora é sua vez de personalisar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
print('=' * 35)