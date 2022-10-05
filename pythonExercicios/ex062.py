print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 62', '-' * 34)
print('-' * 23, 'Dez primeiros termos de uma PA 2.0', '-' * 23)
print('=-' * 41)
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Agora a sua razão: '))
i = 1
i2 = 0
add = 0
while i <= 10:
    print('{}º termo: {}'.format(i, p + (i * r)))

    if i == 10:
        print('Digite quantos termos a mais deseja mostrar: \n')
        add = int(input())
        i2 = i+add
        while add != 0:
            for t in range(i, i2+1):
                print('{}º termo: {}'.format(t, p + (t * r)))
            i = i2
            print('Digite quantos termos a mais deseja mostrar: \n')
            add = int(input())
            i2 = i+add
    i += 1
