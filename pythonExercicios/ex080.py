print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 80', '-' * 34)
print('-' * 25, 'Lendo 5 Números e Ordenando-os', '-' * 25)
print('=-' * 41)
lista = []
n, maior = 0, 0
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        maior = n
        lista.append(n)
        print('Adicionado ao final da lista...')
    elif i == 1:
        if n < maior:
            lista.insert(0, n)
            print(f'Adicionado a posição {i-1} da lista...')
        else:
            lista.append(n)
            maior = n
            print('Adicionado ao final da lista...')
    else:
        if n > maior:
            lista.append(n)
            print('Adicionado ao final da lista...')
            maior = n
        if n < lista[0]:
            lista.insert(0, n)
            print(f'Adicionado a posição {lista.index(n)} da lista...')
        else:
            if len(lista) == 3:
                if n > lista[1]:
                    lista.insert(2, n)
                    print(f'Adicionado a posição {lista.index(n)} da lista...')
                elif n < lista[1]:
                    lista.insert(1, n)
                    print(f'Adicionado a posição {lista.index(n)} da lista...')
            else:
                if n > lista[1] and n > lista[2]:
                    lista.insert(3, n)
                    print(f'Adicionado a posição {lista.index(n)} da lista...')
                elif n > lista[1]:
                    lista.insert(2, n)
                    print(f'Adicionado a posição {lista.index(n)} da lista...')
                elif n < lista[1]:
                    lista.insert(1, n)
                    print(f'Adicionado a posição {lista.index(n)} da lista...')
print(f'{"-="*25}')
print(f'Os valores digitados em ordem foram {lista}')
