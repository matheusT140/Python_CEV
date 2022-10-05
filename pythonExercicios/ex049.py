print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 49', '-' * 34)
print('-' * 30, 'Programa de Tabuada', '-' * 31)
print('=-' * 41)
n = int(input('Digite o número: '))
for i in range (1, 11):
    print('{} x {} = {}.'.format(n, i, n*i))
