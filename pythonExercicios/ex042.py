print('=-'*31)
print('-'*25, 'EXERCÍCIO 42', '-'*25)
print('-'*10, 'Condição de existência e tipo do triângulo', '-'*10)
print('=-'*32)
print('Informe a medida dos lados do triângulo hipotético: ')
a = float(input())
b = float(input())
c = float(input())

if c > a+b or a > c+b or b > c+a:
    print('Os lados informados não podem formar um triângulo.')
else:
    if a != b != c:
        print('Os lados formam um triângulo do tipo escaleno.')
    elif a == b == c:
        print('Os lados formam um triângulo do tipo equilátero.')
    else:
        print('Os lados formam um triângulo do tipo isósceles.')
