print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 104', '-' * 33)
print('-' * 22, 'Função - Validando Entrada de Dados', '-' * 23)
print('=-' * 41)


class cor:
    red = '\33[31m'
    reset = '\33[m'


def leiaInt(s):
    n2 = input(f'{s}')
    if n2.isnumeric():
        return int(n2)
    else:
        print(f'{cor.red}ERRO! Digite um número inteiro válido.{cor.reset}')
        return leiaInt(s)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
