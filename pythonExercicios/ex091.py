from random import randint
from operator import itemgetter
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 91', '-' * 34)
print('-' * 31, 'Programa de Jogo', '-' * 33)
print('=-' * 41)
dicJogadores = {}
dicColoc = []
for i in range(1, 5):
    dicJogadores["jogador" + str(i)] = randint(1, 6)
dicColoc = sorted(dicJogadores.items(), key=itemgetter(1), reverse=True) #dicJogadores.items() - os elementos que serão ordenados
#funç itemgetter vai ordenar os itens; parametro 0 ou 1, para ordenar as chaves ou os valores
print('Valores sorteados:')
for i, j in dicJogadores.items():
    print(f'   O {i} tirou {j}')
print('-='*20)
print('== RANKING DOS JOGADORES ==')
for i, j in enumerate(dicColoc):
    print(f'   {i+1}º lugar: {j[0]} com {j[1]}.')
