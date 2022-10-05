print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 69', '-' * 34)
print('-' * 30, 'Lendo idade e gênero', '-' * 30)
print('=-' * 41)
mais18, contHomens, menos20M = 0, 0, 0
idade = 0
sexo = ''
while True:
    print('-' * 26)
    print('   CADASTRE UMA PESSOA   ')
    print('-' * 26)
    while idade <= 0:
        idade = int(input('Idade: '))
    while sexo != 'm' and sexo != 'f':
        sexo = str(input('Sexo: [M/F] ')).lower()
    if idade > 18:
        mais18 += 1
    if sexo == 'm':
        contHomens += 1
    elif idade < 20:
        menos20M += 1
    print('-' * 26)
    escolha = str(input('Quer continuar? [S/N] ')).lower()
    while escolha != 's' and escolha != 'n':
        escolha = str(input('Quer continuar? [S/N] ')).lower()
    if escolha == 'n':
        print('=======FIM DO PROGRAMA=======')
        print(f'Total de pessoas com mais de 18 anos: {mais18}.')
        if contHomens == 0:
            print('Nenhum homem foi cadastrado.')
        elif contHomens == 1:
            print(f'Ao todo temos um homem cadastrado.')
        else:
            print(f'Ao todo temos {contHomens} homens cadastrados.')
        if menos20M == 1:
            print('E temos uma mulher com menos de 20 anos.')
        elif menos20M == 0:
            print('Não temos nenhuma mulher com menos de 20 anos.')
        else:
            print(f'E temos {menos20M} mulheres com menos de 20 anos.')
        break
    else:
        idade = 0
        sexo = ''
