def titulo(frase):
    print("-" * 20), print(f'{frase:^20}'), print("-" * 20)


titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')


def contador(* num):
    print(num)


contador(5, 1, 5, 8, 9)
contador(1, 2)
# a função contador vai receber uma quantidade variável de parâmetros, podendo ser 1 ou vários números
# joga os parâmetros em uma tupla
