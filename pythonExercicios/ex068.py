from random import randint
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 68', '-' * 34)
print('-' * 27, 'Programa de Par ou Ímpar', '-' * 29)
print('=-' * 41)
escolha = ''
contador = 0
while True:
    n = randint(0, 10)
    nJogador = int(input('Diga um valor: '))
    escolha = str(input(' Par ou Ímpar? [P/I] ')).upper()
    print('_' * 30)
    if (n + nJogador) % 2 == 0 and escolha == 'P':
        contador += 1
        print(f'Você jogou {nJogador} e o computador {n}. Total de {n+nJogador} DEU PAR')
        print('_' * 30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
    elif (n + nJogador) % 2 != 0 and escolha == 'I':
        contador += 1
        print(f'Você jogou {nJogador} e o computador {n}. Total de {n + nJogador} DEU ÍMPAR')
        print('_' * 30)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
    else:
        if (n + nJogador) % 2 != 0:
            print(f'Você jogou {nJogador} e o computador {n}. Total de {n + nJogador} DEU ÍMPAR')
            print('_' * 30)
            print('Você PERDEU!')
            print('=-' * 15)
            print(f'GAME OVER! Você venceu {contador} vezes.')
        else:
            print(f'Você jogou {nJogador} e o computador {n}. Total de {n + nJogador} DEU PAR')
            print('_' * 30)
            print('Você PERDEU!')
            print('=-' * 15)
            print(f'GAME OVER! Você venceu {contador} vezes.')
        break
