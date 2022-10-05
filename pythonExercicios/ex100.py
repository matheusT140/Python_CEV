from time import sleep
from random import randint
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 100', '-' * 34)
print('-' * 28, 'Função - Sortear e Somar', '-' * 28)
print('=-' * 41)


def sorteia():
    l = list()
    print('Sorteando 5 valores da lista: ', end='')
    sleep(3)
    for i in range(0, 5):
        l.append(randint(1, 10))
        sleep(1)
        print(f'{l[i]} ', end='')
    sleep(1)
    print('PRONTO!')
    return l


def somaPar(lista):
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares += i
    print(f'Somando os valores pares de ', end='')
    sleep(1)
    print(f'{lista}...', end='')
    sleep(2)
    print(f' Temos {pares}.')
    sleep(2)
somaPar(sorteia())
