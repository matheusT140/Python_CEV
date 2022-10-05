from time import sleep
print('=-'*32)
print('-'*25, 'EXERCÍCIO 46', '-'*25)
print('-'*15, 'Contagem para fogos de artifício', '-'*15)
print('=-'*32)
print('Iniciando contagem')
sleep(1)
for c in range (10, 0, -1):
    print('{}...'.format(c))
    sleep(1)
print('PEW PEW PEW fogos estouram')
