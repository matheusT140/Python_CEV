from math import hypot
print('{:=^31}'.format('Exercício 017'))
a = float(input('Cateto adjacente: '))
o = float(input('Cateto oposto: '))
print('O valor da hipotenusa é {:.2f}.'.format(hypot(a, o)))
