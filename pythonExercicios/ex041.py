from datetime import date
print('=-'*20)
print('-'*13, 'EXERCÍCIO 41', '-'*13)
print('-'*3, 'Programa de Categoria de Natação', '-'*3)
print('=-'*20)
print('Qual o ano de nascimento do atleta? ')
btd = int(input())
a = date.today().year - btd
if a < 10:
    print('Categoria: MIRIM')
elif a < 15:
    print('Categoria: INFANTIL')
elif a < 20:
    print('Categoria: JUNIOR')
elif a < 21:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
