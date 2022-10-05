from time import sleep
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 98', '-' * 34)
print('-' * 31, 'Função - Contador', '-' * 32)
print('=-' * 41)


def contador(inicio, fim, passo):
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    if inicio > fim:
        passo *= -1
        for i in range(inicio, fim - 1, passo):
            sleep(1)
            print(f'{i} ', end='')
        sleep(1)
        print('FIM!')
        sleep(1)
    elif fim > inicio:
        for i in range(inicio, fim + 1, passo):
            sleep(1)
            print(f'{i} ', end='')
        sleep(1)
        print('FIM!')
        sleep(1)


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input(f'{"Fim:":<8}'))
p = int(input(f'{"Passo:":<8}'))
contador(ini, fim, p)
