'''def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 8, 9, 56, 65, 32]
dobrar(valores)
print(valores)'''

def calculoarea(largura, compri):
    area = largura * compri
    print(f'A área de um terreno {largura} x {compri} é de {area:.1f}m2.')


print(' Controlo de terreno')
print('-' * 21)
largura = float(input('LARGURA (m): '))
compri = float(input('COMPRIMENTO (m): '))
calculoarea(largura, compri)
