print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 83', '-' * 34)
print('-' * 30, 'Analisando expressão', '-' * 30)
print('=-' * 41)
exp = str(input('Digite a expressão: '))
listaP = []
abriu, fechou = 0, 0
for c in exp:
    if c == '(' or c == ')':
        listaP.append(c)
if len(listaP) % 2 == 0:
    for c in listaP:
        if fechou > abriu:
            break
        if c == '(':
            abriu += 1
        if c == ')':
            fechou += 1
if fechou == abriu:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
