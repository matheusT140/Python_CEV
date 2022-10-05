print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 64', '-' * 34)
print('-' * 27, 'Leitura de Vários Números', '-' * 28)
print('=-' * 41)
nTotal = 0
n = int(input('Digite um número : '))
contador = 1
if n == 999:
    contador = 0
while n != 999:
    if n != 999:
        nTotal += n
        contador += 1
        n = int(input('Digite novamente ("999" para encerrar): '))
print('Quantidade de números digitados: {}.\nSoma  entre eles: {}.'.format(contador-1, nTotal))
