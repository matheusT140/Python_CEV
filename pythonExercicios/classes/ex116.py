print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 116', '-' * 33)
print('-' * 28, 'Criando classe Quadrado', '-' * 29)
print('=-' * 41)


class Quadrado:
    def __init__(self, l='1m'):
        self.lado = l

    def mudaLado(self, l):
        self.lado = l

    def retornaLado(self):
        l = ''
        for i in self.lado:
            if i.isnumeric():
                l += i
        return int(l)

    def Area(self):
        l = self.retornaLado()
        return l*l

q = Quadrado('10m')
print(q.retornaLado())
print(q.Area())
