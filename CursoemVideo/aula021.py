def exemplo():
    """
    Doc da função exemplo. Aqui ficam instruções
    sobre a função em questão.
    Descrição: escreve na tela: 'Função exemplo executada.'
    """
    print('Função exemplo executada.')
help(exemplo)


def teste():
    print(f'{"Sem comando ´global´ em ´a´"}')
    a = 1
    b = 2
    c = 3
    print(f'"a" local: {a}')
    print(f'"b" local: {b}')
    print(f'"c" local: {c}')
    print('-' * 20)


def teste2():
    global a
    a = 1
    b = 2
    c = 3
    print(f'{"Com comando ´global´ em ´a´"}')
    print(f'"a" local: {a}')
    print(f'"b" local: {b}')
    print(f'"c" local: {c}')
    print('-'*20)


a = -1
print(f'"a" global {a}')
print('-'*20)
teste()
teste2()
print(f'"a" global {a}')
print('-'*20)
teste()
print(f'"a" global {a}')
# 'a' global continua sendo 1 no final do programa
