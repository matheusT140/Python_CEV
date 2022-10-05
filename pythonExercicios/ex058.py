from random import randint
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 58', '-' * 34)
print('-' * 25, 'Adivinhar número entre 0 e 10', '-' * 26)
print('=-' * 41)
n = randint(0, 10)
n2 = int(input('Desafio. Tente adivinhar qual número a máquina "pensou", entre 0 e 10.\n'))
c = 1
while n2 != n:
    print('Número errado. Tente novamente.')
    n2 = int(input())
    c += 1
print('Parabéns, você acertou. Tentativas até acertar: {}.'.format(c))
