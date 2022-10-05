print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 94', '-' * 34)
print('-' * 27, 'Cadastro de Várias Pessoas', '-' * 27)
print('=-' * 41)
pessoas = list()
individuo = dict()
while True:
    individuo["nome"] = str(input('Nome: '))
    while True:
        individuo["sexo"] = str(input('Sexo [M/F]: ')).upper()
        if individuo["sexo"] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    individuo["idade"] = int(input('Idade: '))
    pessoas.append(individuo.copy())
    individuo.clear()
    while True:
        resp = str(input('Continuar cadastro [S/N]? ')).lower()
        if resp in 'sn':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'n':
        break
mulheres = ''
med = 0
for i, j in enumerate(pessoas):
    med += j["idade"]
    if j["sexo"] == 'F':
        mulheres += j["nome"]+' '
med = med/len(pessoas)
print(f'{"-="*30}')
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {med:.2f} anos.')
print(f'- As mulheres cadastradas foram: {mulheres}')
print(f'- Lista de pessoas que estão acima da média:')
for i, j in enumerate(pessoas):
    if j["idade"] > med:
        print('')
        for k, l in j.items():
            print(f'{k} = {l}; ', end='')
print('')
print('<< ENCERRADO >>')
