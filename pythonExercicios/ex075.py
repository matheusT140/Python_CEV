print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 75', '-' * 34)
print('-' * 30, 'Lendo quatro valores', '-' * 30)
print('=-' * 41)
contPar = 0
t = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {t}')
print(f'O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 foi digitado na posição {t.index(3)}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram', end=' ')
for numero in t:
    if numero % 2 == 0:
        print(f'{numero}', end= ' ')
