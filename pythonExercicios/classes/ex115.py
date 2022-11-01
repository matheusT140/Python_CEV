print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 115', '-' * 33)
print('-' * 30, 'Criando classe Bola', '-' * 31)
print('=-' * 41)


class Bola:
    def __init__(self, cor='branca', circ='70cm', material='couro'):
        self.cor = cor
        self.circ = circ
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(f'{self.cor}')
bolaTeste = Bola('preta', '50cm', 'borracha')
bolaTeste.mostraCor()
bolaTeste.trocaCor('azul')
bolaTeste.mostraCor()
