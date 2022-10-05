print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 89', '-' * 34)
print('-' * 30, 'Dicionário de Notas', '-' * 31)
print('=-' * 41)
aluno_media = dict()
aluno_media["Nome"] = str(input('Nome: '))
aluno_media["Media"] = float(input(f'Média de {aluno_media["Nome"]}: '))
if aluno_media["Media"] >= 6:
    aluno_media["Situação"] = 'Aprovado'
else:
    aluno_media["Situação"] = 'Reprovado'
for i, j in aluno_media.items():
    print(f'{i} é igual a {j}')
