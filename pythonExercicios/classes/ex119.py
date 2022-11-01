print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 119', '-' * 33)
print('-' * 28, 'Criando Classe Conta Corrente', '-' * 28)
print('=-' * 41)


class ContaCorrente:
    """ Classe para uma conta corrente
     - 1º arg: 'codigo', numero e/ou letras; passado para a instância como string
     - 2º arg: 'nome', numero e/ou letras; passado para a instância como string
     - 3º arg: 'saldo'(opcional), numero; passado para a instância como float
     f. altNome(): altera nome da instância e recebe argumento valor string
     f. depósito(): adiciona saldo da instância e recebe argumento valor float
     f. saquet(): retira saldo da instância e recebe argumento valor float"""
    def __init__(self, codigo, nome, saldo=0):
        self.numero = str(codigo)
        self.nome = str(nome)
        self.saldo = float(saldo)

    def altNome(self, nome):
        self.nome = str(nome)

    def depósito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor
