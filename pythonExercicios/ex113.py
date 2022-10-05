print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 113', '-' * 33)
print('-' * 24, 'Função - Aprofundadas em Python', '-' * 25)
print('=-' * 41)


class cor:
    red = '\33[31m'
    reset = '\33[m'


def leiaN():
    while True:
        try:
            n1 = int(input('Digite um numero Inteiro: '))
        except (ValueError, TypeError):
            print(f'{cor.red}Digite um número inteiro válido.{cor.reset}')
            continue
        except KeyboardInterrupt:
            print(f'\n{cor.red}O usuário preferiu não digitar o número{cor.reset}')
            n1 = 0
            break
        else:
            break
    while True:
        try:
            n2 = float(input('Digite um numero Real: '))
        except (ValueError, TypeError):
            print(f'{cor.red}Digite um número real válido.{cor.reset}')
            continue
        except KeyboardInterrupt:
            print(f'\n{cor.red}O usuário preferiu não digitar o número{cor.reset}')
            n2 = 0
            break
        else:
            break
    return f'O valor inteiro digitado foi {n1} e o real foi {n2}.'
print(leiaN())
