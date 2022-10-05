def aumentar(n, p, show):
    p = 1 + (p/100)
    return moeda(n * p, show)


def diminuir(n, p, show):
    p = 1 - (p/100)
    return moeda(n * p, show)


def metade(n, show):
    return moeda(n/2, show)


def dobro(n, show):
    return moeda(n*2, show)


def moeda(num, show=True):
    if show:
        return str(f'R${num:.2f}')
    return str(f'{num:.2f}')


def resumo(n, a, r, show=True):
    print('\033[0;34m-' * 35)
    print(f'\033[1m{"RESUMO DO VALOR":^35}\033[m')
    print('\033[0;34m-' * 35)
    print(f'{"Preço analisado:":<23}{moeda(n, show):<12}')
    print(f'{"Dobro do preço:":<23}{dobro(n, show):<12}')
    print(f'{"Metade do preço:":<23}{metade(n, show):<12}')
    print(f'{(str(a) + "% de aumento:"):<23}{aumentar(n, 10, show):<12}')
    print(f'{(str(r) + "% de redução:"):<23}{diminuir(n, 13, show):<12}')
    print('-' * 35, '\033[m')
