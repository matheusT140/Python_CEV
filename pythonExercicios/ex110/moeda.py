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
        #n1 = ((num % 1)*10)//1
        #n2 = (((num % 1)*10) % 1)*10
        #return str(f'R${(num//1):.0f},{n1:.0f}{n2:.0f}')
                        #minha solução
        return str(f'R${num:.2f}').replace('.', ',')
    return num


def resumo(n, a, r):
    print('-'*35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    print(f'{"Preço analisado:":<18}{moeda(n):<12}')
    print(f'{"Dobro do preço:":<18}{dobro(n, True):<12}')
    print(f'{"Metade do preço:":<18}{metade(n, True):<12}')
    print(f'{(str(a) +"% de aumento:"):<18}{aumentar(n, 10, True):<12}')
    print(f'{(str(r) + "% de redução:"):<18}{diminuir(n, 13, True):<12}')
    print('-' * 35)
