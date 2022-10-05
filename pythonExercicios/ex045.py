from random import randint
from time import sleep
print('=-'*32)
print('-'*25, 'EXERCÍCIO 45', '-'*25)
print('-'*15, 'Jokenpô - Pedra - Papel - Tesoura', '-'*14)
print('=-'*32)
PPT = ['Pedra', 'Papel', 'Tesoura']
player = int(input('Jokenpô! Escolha entre:\n'
                   '[1] Pedra\n[2] Papel\n[3] Tesoura\n '))
computer = randint(1, 3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('MÁQUINA: {}\n       X\nJOGADOR: {}'.format(PPT[computer-1], PPT[player-1]))
sleep(1)
if computer != player:
    if computer == 1:
        if player == 3:
            print('MAQUINA VENCE!')
        else:
            print('JOGADOR VENCE!')
    elif computer == 3:
        if player == 2:
            print('MÁQUINA VENCE!')
        else:
            print('JOGADOR VENCE!')
    elif computer == 2:
        if player == 1:
            print('MÁQUINA VENCE!')
        else:
            print('JOGADOR VENCE!')
else:
    print('EMPATE!')