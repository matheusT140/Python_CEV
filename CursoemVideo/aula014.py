#quantidade de numeros pares e impares digitados
pares = impares = 0
print('CONTADOR DE NÚMEROS PARES E IMPARES\n(digite 0 para encerrar)')
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print('\nPares digitados: {}.\nÍmpares digitados: {}.'.format(pares, impares))
