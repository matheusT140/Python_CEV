print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 89', '-' * 34)
print('-' * 26, 'Programa de Notas Escolares', '-' * 27)
print('=-' * 41)
lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append([nome, [nota1, nota2]])
    resp = str(input('Quer continuar? [S/N]')).lower()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar? [S/N]')).lower()
    if resp == 'n':
        break
print(f'{"-="*25}')
print(f'Nº  NOME {"MEDIA":>12}')
print('-'*27)
for i, aluno in enumerate(lista):
    nome = aluno[0]
    media = (aluno[1][0] + aluno[1][1])/2
    print(f'{i:<4}{nome:<12}{media:>5.1f}')
print('-'*35)
while True:
    i = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if i == 999:
        break
    print(f'Notas de {lista[i][0]} são {lista[i][1]}')
    print('-' * 35)
