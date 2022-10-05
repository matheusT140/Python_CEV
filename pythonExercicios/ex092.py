from datetime import date
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 92', '-' * 34)
print('-' * 27, 'Programa de Aposentadoria', '-' * 28)
print('=-' * 41)
cadastro = dict()
cadastro["nome"] = str(input('Nome: '))
cadastro["idade"] = int(input('Ano de Nascimento: '))
cadastro["ctps"] = int(input('Carteira de Trabalho (0 - não tem): '))
if cadastro["ctps"] == 0:
    print(f'{"-=" * 25}')
    print(cadastro)
    for i, j in cadastro.items():
        if i == 'idade':
            data = date.today()
            print(f'{i}: {data.year - j}')
        else:
            print(f'{i}: {j}')
else:
    cadastro["contratação"] = int(input('Ano de contratação: '))
    cadastro["salário"] = int(input('Salário: R$ '))
    print(f'{"-=" * 25}')
    print(cadastro)
    for i, j in cadastro.items():
        if i == 'idade':
            data = date.today()
            print(f'{i}: {data.year - j}')
        else:
            print(f'{i}: {j}')
    aposentadoria = (data.year - cadastro["idade"]) + (35 - (data.year - cadastro["contratação"]))
    print(f'Aposentadoria: {aposentadoria}')
