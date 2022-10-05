print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 78', '-' * 34)
print('-' * 32, 'Lista de 5 valores', '-' * 30)
print('=-' * 41)
lista = []
maior, menor = 0, 0
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior, menor = lista[i], lista[i]
    else:
        if maior > lista[i]:
            maior = lista[i]
        if menor < lista[i]:
            menor = lista[i]
print(f'{"=-"*25}')
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na posição', end=' ')
for i, j in enumerate(lista):
    if j == maior:
        print(f'{i}...', end=' ')
print('')
print(f'O menor valor digitado foi {menor} na posição', end=' ')
for i, j in enumerate(lista):
    if j == menor:
        print(f'{i}...', end=' ')
