def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)

def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)

def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def prec(preco):
    return preco


def resumo(preco=0, aumento=7, reduzir=3):
    moed = moeda(preco)
    aum = aumentar(preco, aumento)
    red = diminuir(preco, reduzir)
    dob = dobro(preco, True)
    met = metade(preco, True)

    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado: \tR${moed}')
    print(f'Dobro do preço: \t{dob}')
    print(f'Metade do preço: \t{met}')
    print(f'{aumento}% de aumento: \t{aum}')
    print(f'{reduzir}% de redução: \t{red}')
    print('-'*30)
