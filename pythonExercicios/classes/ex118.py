print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 118', '-' * 33)
print('-' * 28, 'Criando classe Pessoa', '-' * 28)
print('=-' * 41)


def mostraPessoa(p):
    print(f'{"-="*15}')
    print(
        f'Nome: {p.nome}.\nIdade: {p.idade} anos.\nPeso: {p.peso} kg.\nAltura: {p.altura // 1:.0f} metro e {(p.altura % 1) * 100:.0f} centímetros.')
    print(f'{"-=" * 15}')


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, n):
        if self.idade < 21:
            self.idade += n
            self.altura += n*0.5
        else:
            self.idade += n

    def engordar(self, n):
        self.peso += n

    def emagrecer(self, n):
        self.peso -= n

    def crescer(self, n):
        self.altura += n

eu = Pessoa('Matheus', 26, 84, 1.79)
mostraPessoa(eu)
eu.engordar(10)
print(f'{"Engordou":^30}')
mostraPessoa(eu)
eu.emagrecer(15)
print(f'{"Emagreceu":^30}')
mostraPessoa(eu)
eu.envelhecer(2)
print(f'{"Envelheceu":^30}')
mostraPessoa(eu)
eu.crescer(0.08)
print(f'{"Cresceu":^30}')
mostraPessoa(eu)
