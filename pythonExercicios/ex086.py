print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 86', '-' * 34)
print('-' * 35, 'Matriz 3x3', '-' * 35)
print('=-' * 41)
matriz = [[], [], []]
for i, linha in enumerate(matriz):
    for coluna in range(0, 3):
        linha.append(int(input(f'Digite um valor para [{i}, {coluna}]: ')))
print(f'{"-="*25}')
for i, linha in enumerate(matriz):
    if i != 0:
        print('')
    for j, coluna in enumerate(linha):
        print(f'[  {coluna}  ]', end='')
