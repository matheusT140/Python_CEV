from math import sin, cos, tan, radians
print('{:=^31}'.format('Exercício 018'))
h = float(input('Digite quantos graus possui o ângulo: '))
print('Seno de {}°: {:.1f}.\nCosseno de {}°: {:.1f}.\nTangente de {}°: {:.1f}.'.format(h, sin(radians(h)), h, cos(radians(h)), h, tan(radians(h))))
