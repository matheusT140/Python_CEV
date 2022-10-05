print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 71', '-' * 34)
print('-' * 32, 'Caixa Eletrônico', '-' * 32)
print('=-' * 41)
print('=' * 25)
print('        BANCO CEV        ')
print('=' * 25)
valor, nota50, nota20, nota10, nota1 = 0, 0, 0, 0, 0
valor = int(input('Que valor você quer sacar? R$'))
while True:
    if valor >= 50:
        nota50 = valor // 50
        valor = valor % 50
    elif valor > 20:
        nota20 = valor // 20
        valor = valor % 20
    elif valor > 10:
        nota10 = valor // 10
        valor = valor % 10
    else:
        nota1 = valor // 1
        valor = valor % 1
    if valor == 0:
        print(f'Total de {nota50} cédulas de R$50')
        print(f'Total de {nota20} cédulas de R$20')
        print(f'Total de {nota10} cédulas de R$10')
        print(f'Total de {nota1} cédulas de R$1')
        print('=' * 25)
        break
