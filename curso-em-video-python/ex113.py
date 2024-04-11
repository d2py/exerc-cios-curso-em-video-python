'''try:
    a = int(input('Numerodor: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
else:
    print(f'O resultado e {r:.1f}')
finally:
    print('Volte sempre, muito Obrigado')'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        except (ValueError, TypeError):
            print('ERRO: por favor digite um valor inteiro válido.')
            continue

        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))

        except (ValueError, TypeError):
            print('ERRO: por favor digite um valor inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return n



nint = leiaInt('Digite um numero INTEIRO: ')
num = leiafloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {nint} e o real foi {num} ')





