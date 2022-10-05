print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 106', '-' * 33)
print('-' * 17, 'Função - Sistema Interativo de Ajuda em Python', '-' * 17)
print('=-' * 41)


def inicio():
    print('\033[0;0;42m', '^'*30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('^'*30)
    print('\33[m', end='')
    r = str(input('Função ou Biblioteca > '))
    return r


def pegaFuncao(r):
    print('\033[0;0;44m', '^' * 42)
    r = "'" + r + "'"
    print(f'{"Acessando o manual do comando " + r:^42}')
    print('^' * 42)
    print('\033[m', end='')


def mostraHelp(r):
    print('\033[7m')
    help(r)


while True:
    r = inicio().lower()
    if r == 'fim':
        print('\033[0;0;41m', end='')
        print('^' * 15)
        print(f'{"ATÉ LOGO!":^15}')
        print('^' * 15)
        break
    pegaFuncao(r)
    mostraHelp(r)
