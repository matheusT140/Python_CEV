print('--Condição de existência do triângulo--')
print('Informe a medida dos lados do triângulo hipotético: ')
a = float(input())
b = float(input())
c = float(input())

if c > a+b or a > c+b or b > c+a:
    print('Os lados informados não podem formar um triângulo.')
else:
    print('Os lados formam um triângulo.')
