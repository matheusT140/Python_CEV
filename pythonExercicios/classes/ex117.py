print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 117', '-' * 33)
print('-' * 28, 'Criando classe Retângulo', '-' * 28)
print('=-' * 41)


class Retângulo:
    def __init__(self, l, c):
        self.ladoA = l
        self.ladoB = c

    def mudarLado(self, l, c):
        self.ladoA = l
        self.ladoB = c

    def mostraLados(self):
        print(f'Largura: {self.ladoA}\nComprimento: {self.ladoB}')

    def area(self):
        a = self.ladoA*self.ladoB
        return a

    def perimetro(self):
        p = (self.ladoA*2)+(self.ladoB*2)
        return p

print(f'{"-="*30}')
print(f'{"Cálculo para quantidade de pisos e rodapés":^60}')
print(f'{"-="*30}')
while True:
    l = input('Informe a largura do local: ')
    c = input('Informe o comprimento do local: ')
    if l.isnumeric() and c.isnumeric():
        l = float(l)
        c = float(c)
        break
    else:
        print('Digite um valor numérico.')
local = Retângulo(l, c)
while True:
    l = input('Informe a largura do piso: ')
    c = input('Informe o comprimento do piso: ')
    if l.isnumeric() and c.isnumeric():
        l = float(l)
        c = float(c)
        break
    else:
        print('Digite um valor numérico.')
piso = (l*c)
rodape = float(input('Informe o comprimento do rodapé: '))
print(f'{"-="*30}')
if local.area() % piso != 0:
    resto = 1
else:
    resto = 0
if local.perimetro() % rodape != 0:
    resto2 = 1
else:
    resto2 = 0
print(f'Serão necessários {(local.area()/piso)+resto:.0f} pisos para o local e {(local.perimetro()/rodape)+resto2:.0f} rodapés')
