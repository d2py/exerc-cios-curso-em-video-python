def titulo(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(txt.center(tam))
    print('~' * tam)

titulo('Diego Dias')
titulo('Fazendo Curso em Video')
titulo('Bem Vindo')
