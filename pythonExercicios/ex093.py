print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 93', '-' * 34)
print('-' * 29, 'Rendimento do jogador', '-' * 30)
print('=-' * 41)
jogador = dict()
jogador["nome"] = str(input('Nome do Jogador: '))
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
lista = list()
gols = jogador["total"] = 0
for i in range(0, p):
    gols = int(input(f'Quantos gols na partida {i + 1}? '))
    lista.append(gols)
jogador["total"] = sum(lista)
jogador["gols"] = lista[:] #dessa forma lista não fica conectada ao item do dicionário
print(f'{"-="*30}')
print(jogador)
print(f'{"-="*30}')
for i, j in jogador.items():
    print(f'{i}: {j}')
print(f'{"-="*30}')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, j in enumerate(jogador["gols"]):
    print(f'    => Na partida {i+1}, fez {j} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
lista.append(10)
print(sum(lista))
print(sum(jogador["gols"]))
