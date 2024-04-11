
def notas(*valor, sit=False):
    alo = {}
    soma = 0
    tot = 0
    menor = maior = 0
    for c in valor:
        soma += c
        tot += 1
        if tot == 1:
             menor = c
        else:
            if c > maior:
                maior = c
            else:
                menor = c
    media = soma / len(valor)
    alo['total'] = len(valor)
    alo['maior'] = maior
    alo['menor'] = menor
    alo['media'] = media
    if sit:
        if media < 4:
            alo['situacao'] = 'RUIM'
        elif media < 8:
            alo['situacao'] = 'BOM'
        else:
            alo['situacao'] = 'OTIMO'
    return alo


#Progama principal
res = notas(5.5, 9.5, 10, sit=True)
print('-=' * 43)
print(res)

