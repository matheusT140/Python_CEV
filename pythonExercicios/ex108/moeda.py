def aumentar(n, p):
    p = 1 + (p/100)
    return n * p


def diminuir(n, p):
    p = 1 - (p/100)
    return n * p


def metade(n):
    return n/2


def dobro(n):
    return n*2


def moeda(num):
    #n1 = ((num % 1)*10)//1
    #n2 = (((num % 1)*10) % 1)*10
    #return str(f'R${(num//1):.0f},{n1:.0f}{n2:.0f}')
                    #minha solução
    return str(f'R${num:.2f}').replace('.', ',')
