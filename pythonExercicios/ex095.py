print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 94', '-' * 34)
print('-' * 28, 'Rendimento de jogadores', '-' * 29)
print('=-' * 41)
jogadores = list()
while True:
    print('-'*32)
    jogador = dict()
    jogador["nome"] = str(input('Nome do Jogador: '))
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    lista = list()
    gols = jogador["total"] = 0
    for i in range(0, p):
        gols = int(input(f'Quantos gols na partida {i + 1}? '))
        lista.append(gols)
    jogador["total"] = sum(lista)
    jogador["gols"] = lista[:]
    jogadores.append(jogador.copy())
    jogador.clear()
    lista.clear()
    print(jogadores)
    resp = str(input('Quer continuar [S/N]? ')).lower()
    if resp == 'n':
        print(f'{"-=" * 30}')
        break
print(f'cod nome{"gols":>18}{"total":>16}')
print('-'*45)
for i, j in enumerate(jogadores):
    print(f'{i:>3} {j["nome"]:<18}{str(j["gols"]):<16}{str(j["total"]):>2}')
print('-'*45)
while True:
    d = int(input('Mostrar dados de qual jogador? '))
    if (len(jogadores) - 1) < d != 999: #(len(jogadores) - 1) - dessa forma se obtem valor máximo do índice
        print(f'ERRO! Não existe jogador com o código {d}! Tente novamente')
        print('-' * 45)
    elif d == 999:
        print('<< VOLTE SEMPRE >>')
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[d]["nome"]}:')
        for i, j in enumerate(jogadores[d]["gols"]):
            print(f'   No jogo {i + 1} fez {j} gols.')
        print('-' * 45)
