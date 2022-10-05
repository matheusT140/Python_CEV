from time import sleep
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 96', '-' * 34)
print('-' * 28, 'Função - Cálculo de Área', '-' * 28)
print('=-' * 41)


def area(l, c):
    print(f'A área de um terreno de {l}x{c} é de {l * c} m².')


print(f'{"Controle de Terrenos":^25}')
print('-' * 25)
sleep(1)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
