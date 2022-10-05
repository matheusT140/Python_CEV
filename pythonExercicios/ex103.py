print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 103', '-' * 33)
print('-' * 27, 'Função - Ficha do Jogador', '-' * 28)
print('=-' * 41)


def fichaJogador(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


print('-'*35)
jogador = str(input('Nome do Jogador: '))
gol = str(input('Número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    fichaJogador(gols=gol)
else:
    fichaJogador(jogador, gol)
