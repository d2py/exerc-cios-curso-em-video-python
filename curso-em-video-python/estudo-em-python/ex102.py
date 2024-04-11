
def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial
    :param n: valor a ser calculado o fatorial
    :param show: (Opcional)Informa se mostra a sequencia da conta
    :return: Mostra o valor do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f



print('-=' * 15)
print(fatorial(5, ))
help(fatorial)
