print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 76', '-' * 34)
print('-' * 33, 'Lista de Preços', '-' * 32)
print('=-' * 41)
t = ('Lápis', float(1.75), 'Borracha', float(2.00), 'Caderno', float(15.90), 'Estojo', float(25.00)
     , 'Transferidor', float(4.20), 'Compasso', float(9.99), 'Mochila', float(120.32)
     , 'Canetas', float(22.30), 'Livro', float(34.90))
print('-' * 41)
print(f'{"LISTAGEM DE PREÇOS":^40}')# '^' centraliza a variável, '40' quantidade de caracteres que ela vai ocupar
print('-' * 41)
n = 0
for i in range(0, len(t)):
    if i % 2 == 0:
        print(f'{t[i]:.<30}', end='')
    else:
        print(f'{t[i]:>7.2f}')# '>' alinha a direita, '7' quantidade de caracteres que a variável vai
        # ocupar, '.2f' formato da casa decimal que ela vai ser mostrada
print('-' * 41)
