print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 63', '-' * 34)
print('-' * 29, 'Sequência de Fibonacci', '-' * 29)
print('=-' * 41)
sequencia = []
s = ''
n = int(input('Primeiro elemento da sequência: '))
contador = 0
nf = int(input('Quantos elementos deseja ver? '))
while contador <= nf+1:
    if contador == 2:
        sequencia += [sequencia[0] + sequencia[1]]
        contador += 1
    elif contador < 2:
        sequencia += [n]
        contador += 1
    elif contador % 3 == 0:
        s += str(sequencia[0]) + ' ' + str(sequencia[1]) + ' ' + str(sequencia[2]) + ' '
        sequencia[0] = sequencia[1] + sequencia[2]
        sequencia[1] = sequencia[0] + sequencia[2]
        sequencia[2] = sequencia[0] + sequencia[1]
        contador += 3
s = s.split()
s2 = ''
contador = 0
while contador <= nf-1:
    if contador % 9 == 0 and contador != 0:
        s2 += s[contador] + '\n'
    if contador < nf-1:
        s2 += s[contador] + ', '
    elif contador == nf-1:
        s2 += s[contador]
    contador += 1
print('Sequência de Fibonacci de {} elementos, a partir de {}:\n {}.'.format(nf, n, s2))
