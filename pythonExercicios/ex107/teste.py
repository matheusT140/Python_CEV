from moeda import *
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 107', '-' * 33)
print('-' * 25, 'Exercitando Módulos em Python', '-' * 26)
print('=-' * 41)
n = float(input('Digite o preço: R$ '))
print(f'A metade de {n} é {metade(n)}')
print(f'O dobro de {n} é {dobro(n)}')
print(f'Aumentando {10}%, temos {aumentar(n, 10):1f}')
print(f'Reduzindo {13}%, temos {diminuir(n, 13):1f}')