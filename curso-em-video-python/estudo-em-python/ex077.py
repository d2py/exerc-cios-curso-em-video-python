palavras = ('padaria', 'comprar', 'psicologia', 'bebedouro',
            'administraçao', 'programa', 'ventilador','comparecer')

for c in palavras:
    print(f'\nNa palavra {c.upper()} temos', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
