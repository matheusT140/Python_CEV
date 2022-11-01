from time import sleep
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 120', '-' * 33)
print('-' * 35, 'Programa Tv', '-' * 34)
print('=-' * 41)


def limpaTela():
    print('\n' * 20)


def mostraTela(r=''):
    if r == 'c':
        print(f'{("-=" * 20):^82}')
        print(f'{"TV - Ligada":^82}')
        print(f'{("-=" * 20):^82}')
        print()
        print(f'{" " * 21}{"Mudar de canal":<20}{" ":>18}', end='')
        while True:
            c = input()
            if c.isnumeric():
                if int(c) < 1 or int(c) > 100:
                    pass
                else:
                    break
        Tv.mudarCanal(Tv(), c)
        limpaTela()
        mostraTela()
    elif r == '+' or r == '-':
        print(f'{("-=" * 20):^82}')
        print(f'{"TV - Ligada":^82}')
        print(f'{("-=" * 20):^82}')
        print(f'{" " * 21}{"Aumentar/Diminuir":<20}{"":>19}', end='')
        while True:
            n = input()
            if n != '+' and n != '-':
                pass
            else:
                break
        if n == '+':
            Tv.aumentarVolume(Tv())
        else:
            Tv.diminuirVolume(Tv())
        limpaTela()
        mostraTela()
    else:
        print(f'{("-=" * 20):^82}')
        print(f'{"TV - Ligada":^82}')
        print(f'{("-=" * 20):^82}')
        print(f'{" " * 21}{"CANAL: " + str(Tv.canal):<20}{"VOLUME: " + str(Tv.volume):>20}')
        print(f'{" " * 21}{"Mudar de canal":<20}{"C":>20}')
        print(f'{" " * 21}{"Aumentar/Diminuir":<20}{"+ | -":>20}')
        print(f'{" " * 21}{"Desligar TV":<20}{"0":>20}')


def programa():
    mostraTela()
    while True:
        print(f'{" ":41}', end='')
        resp = input().lower()
        if resp == '0':
            print(f'{"Encerrando":>41}', end='')
            for j in range(1, 4):
                sleep(1)
                print('.', end='')
            sleep(1)
            break
        limpaTela()
        mostraTela(resp)


class Tv:
    canal = 1
    volume = 15

    def aumentarVolume(self):
        Tv.volume += 1

    def diminuirVolume(self):
        Tv.volume -= 1

    def mudarCanal(self, n):
        Tv.canal = n


programa()
