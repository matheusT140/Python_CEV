print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 67', '-' * 34)
print('-' * 25, 'Tabuada de um numero ou vários', '-' * 25)
print('=-' * 41)
while True:
    n = int(input('Quer ver tabuada de qual valor? '))
    if n < 0:
        break
    print('_' * 31)
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('_' * 31)
