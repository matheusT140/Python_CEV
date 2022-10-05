from random import randint
from time import sleep
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 88', '-' * 34)
print('-' * 31, 'Jogos da Mega Sena', '-' * 31)
print('=-' * 41)
print(f'{"-"*31}')
print(f'{"JOGO NA MEGA SENA":^31}')
print(f'{"-"*31}')
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{("-="*3) + "  SORTEANDO " + str(jogos) + " JOGOS  " + ("-="*3)}')
listaJogos = [[]]
for i in range(0, jogos):
    if i != 0:
        listaJogos.append([])
    for j in range(0, 6):
        listaJogos[i].append(randint(1, 60))
for i, jogo in enumerate(listaJogos):
    sleep(2)
    jogo.sort()
    print(f'Jogo {i+1}: {jogo}')
sleep(2)
