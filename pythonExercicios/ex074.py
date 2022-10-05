from random import randint
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 74', '-' * 34)
print('-' * 28, 'Cinco números aleatórios', '-' * 28)
print('=-' * 41)
nTupla = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))
print(f'os valores sorteados foram:', end=' ')
for numeros in nTupla:
    print(f'{numeros}', end=' ')
print(f'\nO maior valor sorteado foi {max(nTupla)}')
# max() e min() função da tupla
print(f'O menor valor sorteado foi {min(nTupla)}')
