print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 55', '-' * 34)
print('-' * 29, 'Verificando maior peso', '-' * 29)
print('=-' * 41)
for i in range(0, 5):
    if i == 0:
        n = float(input('Informe o peso da {}ª pessoa: '.format(i+1)))
        maior = n
        menor = n
    else:
        n2 = float(input('Informe o peso da {}ª pessoa: '.format(i+1)))
        if n2 > maior:
            maior = n2
        if n2 < menor:
            menor = n2
print('O maior peso foi {} KG e o menor foi {} KG.'.format(maior, menor))
