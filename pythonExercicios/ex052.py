print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 52', '-' * 34)
print('-' * 26, 'Verificador de número primo', '-' * 27)
print('=-' * 41)
n = int(input('Digite o número a ser verificado: '))
contador = 0
for i in range(1, n+1):
    if n % i == 0:
        contador += 1
if contador <= 2:
    print('O número {} é um número primo.'.format(n))
else:
    print('O número {} não é um número primo.'.format(n))
