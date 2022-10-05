print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 84', '-' * 34)
print('-' * 30, 'Cadastrando pessoas', '-' * 31)
print('=-' * 41)
pessoas = []
maior, menor, cont, cont2 = 0, 0, 0, 0
while True:
    resp = ''
    nome = str(input('Nome: '))
    peso = int(input('Peso: '))
    pessoas.append([nome, peso])
    if len(pessoas) == 1:
        maior, menor = peso, peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
    while resp != 'n' and resp != 's':
        resp = str(input('Quer continuar? [S/N] ')).lower()
    if resp == 'n':
        break
print(f'{"-="*25}')
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de', end='')
for p in pessoas:
    cont2 += p.count(maior)
for p in pessoas:
    if maior == p[1]:
        if cont == cont2-1 and cont != 0:
            print(f' e {p[0]}', end='')
            cont += 1
        elif cont == 0:
            print(f' {p[0]}', end='')
            cont += 1
        else:
            print(f', {p[0]}', end='')
            cont += 1
print('.')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de', end='')
cont = 0
cont2 = 0
for p in pessoas:
    cont2 += p.count(menor)
for p in pessoas:
    if menor == p[1]:
        if cont == cont2 - 1 and cont != 0:
            print(f' e {p[0]}', end='')
            cont += 1
        elif cont == 0:
            print(f' {p[0]}', end='')
            cont += 1
        else:
            print(f', {p[0]}', end='')
            cont += 1
print('.')
