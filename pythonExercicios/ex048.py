print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 48', '-' * 34)
print('-' * 25, 'Soma dos n° ímpares de 1 a 500', '-' * 25)
print('-' * 33, 'múltiplos de 3', '-' * 33)
print('=-' * 41)
s = 0
for i in range(3, 501):
    if i % 3 == 0 and i % 2 != 0:
        s += i
print(s)
