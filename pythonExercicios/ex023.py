numero = input('Digite um numero de 0 a 9999: ')
u = int(numero) % 10
d = int(numero) // 10 % 10
c = int(numero) // 100 % 10
m = int(numero) // 1000
print('unidade: {}.'.format(u))
print('dezena: {}.'.format(d))
print('centena: {}.'.format(c))
print('milhar: {}.'.format(m))
