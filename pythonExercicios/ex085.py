print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 85', '-' * 34)
print('-' * 28, 'Lista de Pares e Ímpares', '-' * 28)
print('=-' * 41)
listaPI = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        listaPI[1].append(n)
    else:
        listaPI[0].append(n)
print(f'{"-="*25}')
listaPI[0].sort()
listaPI[1].sort()
print(f'Os valores pares digitados foram: {listaPI[1]}')
print(f'Os valores ímpares digitados foram: {listaPI[0]}')
