print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 66', '-' * 34)
print('-' * 26, 'Leitura de Vários Números 3', '-' * 27)
print('=-' * 41)
n = int(input('Digite um número: '))
contador, total = 0, 0
while True:
    if n == 999:
        break
    contador += 1
    total += n
    n = int(input('Digite novamente (sair - 999): '))
print(f'A soma dos {total} valores foi {contador}.')
