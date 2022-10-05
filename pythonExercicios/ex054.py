from datetime import date
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 54', '-' * 34)
print('-' * 24, 'Verificar maioridade das pessoas', '-' * 24)
print('=-' * 41)
n, menor, maior = 0, 0, 0 #forma de atribuição de várias variáveis em uma mesma linha
print('Informe o ano de nascimento das 6 pessoas: ')
for i in range(0, 6):
    n = int(input())
    if date.today().year - n > 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas já atingiram a maioridade e {} são de menores.'.format(maior, menor))
