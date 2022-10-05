print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 87', '-' * 34)
print('-' * 37, 'Matriz 3x3 2.0', '-' * 37)
print('=-' * 41)
matriz = [[], [], []]
parSoma, coluna3Soma, maior2linha = 0, 0, 0
for i, linha in enumerate(matriz):
    for coluna in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{i}, {coluna}]: ')))
print(f'{"-="*25}')
for i, linha in enumerate(matriz):
    if i != 0:
        print('')
    for j, coluna in enumerate(linha):
        print(f'[  {coluna}  ]', end='')
for i, linha in enumerate(matriz):
    coluna3Soma += linha[2]
    for j, coluna in enumerate(linha):
        if coluna % 2 == 0:
            parSoma += coluna
        if i == 1:
            if j == 0:
                maior2linha = coluna
            else:
                if coluna > maior2linha:
                    maior2linha = coluna
print(f'\n{"-="*25}')
print(f'A soma dos valores pares é {parSoma}.')
print(f'A soma dos valores da terceira coluna é {coluna3Soma}.')
print(f'O maior valor da segunda linha é {maior2linha}.')
