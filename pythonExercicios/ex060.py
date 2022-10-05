print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 60', '-' * 34)
print('-' * 36, 'Fatorial', '-' * 36)
print('=-' * 41)
n = int(input('Digite um número inteiro maior que 0.\n'))
fat = 1
n2 = n
while n2 != 1:
    fat *= n2
    n2 -= 1
print('O fatorial de {} é {}.'.format(n, fat))
