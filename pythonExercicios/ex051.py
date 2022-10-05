print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 51', '-' * 34)
print('-' * 25, 'Dez primeiros termos de uma PA', '-' * 25)
print('=-' * 41)
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Agora a sua razão: '))
for i in range(0, 10):
    print('{}º termo: {}'.format(i+1, p + (i*r)))
