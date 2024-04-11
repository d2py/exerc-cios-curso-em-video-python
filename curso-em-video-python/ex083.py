
expre=(str(input('Digite sua expressão: ')))
expr = []
for v in expre:
    if v == '(':
        expr.append('(')

    elif v == ')':
        if len(expr) > 0:
            expr.pop()
        else:
            expr.append(')')
            break
if len(expr) == 0:
    print('Sua expressão esta valida ')
else:
    print('Sua expressão esta invalida')

