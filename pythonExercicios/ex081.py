print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 81', '-' * 34)
print('-' * 30, 'Lendo Vários Números', '-' * 30)
print('=-' * 41)
lista = [int(input('Digite um valor: '))]
cont = 1
resp = ''
while True:
    resp = str(input('Quer continuar? [S/N]')).lower()
    while True:
        if resp != 'n' and resp != 's':
            resp = str(input('Quer continuar? [S/N]')).lower()
        else:
            break
    if resp == 'n':
        break
    else:
        lista.append(int(input('Digite um valor: ')))
        cont += 1
print(f'{"-="*25}')
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
