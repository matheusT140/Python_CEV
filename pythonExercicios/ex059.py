print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 59', '-' * 34)
print('-' * 26, 'Operações entre dois valores', '-' * 26)
print('=-' * 41)
print('Operações com dois valores. Digite um número: ')
n = int(input())
n2 = int(input('Agora outro número.\n'))
option = 0
while option != 5:
    print('Escolha a operação desejada:')
    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos valores\n'
          '[ 5 ] sair do programa\n')
    option = int(input())
    if option == 1:
        print('A soma de {} mais {} é igual a {}.'.format(n, n2, n+n2))
        input('Pressione qualquer tecla para voltar ao menu.')
    elif option == 2:
        print('{} vezes {} é igual a {}.'.format(n, n2, n*n2))
        input('Pressione qualquer tecla para voltar ao menu.')
    elif option == 3:
        if n > n2:
            print('{} é maior que {}.'.format(n, n2))
        elif n < n2:
            print('{} é maior que {}.'.format(n2, n))
        else:
            print('{} e {} são iguais.'.format(n, n2))
        input('Pressione qualquer tecla para voltar ao menu.')
    elif option == 4:
        print('Opção "novos valores" escolhida')
        n = int(input('Informe o primeiro n°\n'))
        n2 = int(input('Informe o segundo n°\n'))
        input('Pressione qualquer tecla continuar.')

