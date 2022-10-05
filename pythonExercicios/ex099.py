from time import sleep
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 99', '-' * 34)
print('-' * 28, 'Função - Descobre Maior', '-' * 29)
print('=-' * 41)


def maior(* n):
    sleep(0.5)
    print('-='*25)
    print('Analisando os valores passados...')
    sleep(3)
    m = 0
    for i in n:
        if i > m:
            m = i
        print(f'{i} ', end='')
        sleep(1)
    print(f' - Foram informados {len(n)} valores ao todo.')
    sleep(2)
    print(f'O maior valor informado foi de {m}.')
    sleep(3)


maior(1, 2, 3, 4, 5)
maior(4, 0, 7)
maior(1, 2)
maior(6)
maior()
