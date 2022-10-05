print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 50', '-' * 34)
print('-' * 30, 'Soma de seis números', '-' * 30)
print('=-' * 41)
soma = 0
for i in range(1, 7):
    n = int(input('Digite o {}º número.\n'.format(i)))
    if n % 2 == 0:
        soma += n
print('A soma dos números digitados que são pares foi: {}.'.format(soma))
