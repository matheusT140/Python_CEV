print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 82', '-' * 34)
print('-' * 30, 'Criando três listas', '-' * 31)
print('=-' * 41)
lista = [int(input('Digite um número: '))]
resp = ''
while True:
    resp = str(input('Quer continuar? [S/N]'))
    while True:
        if resp != 'n' and resp != 's':
            resp = str(input('Quer continuar? [S/N]')).lower()
        else:
            break
    if resp == 's':
        lista.append(int(input('Digite um número: ')))
    else:
        break
print(f'{"-="*25}')
listaPar = []
listaImpar = []
for i in lista:
    if i % 2 == 0:
        listaPar.append(i)
    else:
        listaImpar.append(i)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')
