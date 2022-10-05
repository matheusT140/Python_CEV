print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 102', '-' * 33)
print('-' * 29, 'Função - Fatorial 2.0', '-' * 30)
print('=-' * 41)


def fatorial(n, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param n: número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor fatorial de um número n.'
    """
    total = 1
    for i in range(n, 0, -1):
        total *= i
        if show:
            if i == 1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
    print(total)


# help(fatorial)
print('-'*35)
numero = int(input('Informe o nº para o fatorial: '))
resp = str(input('Deseja ver o processo? [S/N] ')).lower()
if resp == 's':
    fatorial(numero, show=True)
elif resp == 'n':
    fatorial(numero)
