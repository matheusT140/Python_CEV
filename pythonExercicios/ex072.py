print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 72', '-' * 34)
print('-' * 31, 'Número por extenso', '-' * 31)
print('=-' * 41)
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
for pos, numero in enumerate(numeros):
    if pos == n:
        print(f'Você digitou o número {numero}')
