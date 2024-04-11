print('='*15)
print('AS 10 TERMOS DE UMA PA')
print('='*15)
pri = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
an = pri + (10-1) * raz
for i in range(pri, an, raz):
    print(i)
print('Acabou')
