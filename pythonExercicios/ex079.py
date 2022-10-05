print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 79', '-' * 34)
print('-' * 31, 'Lendo Vários Números', '-' * 29)
print('=-' * 41)
n = 0
lista = list()
escolha = ''
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valores já existentes não serão adicionados.')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    escolha = str(input('Quer continuar? [S/N]')).lower()
    if escolha == 'n':
        break
lista.sort()
print(f'{"-="*25}')
print(f'Você digitou os valores {lista}')
