print('=-'*20)
print('-'*13, 'EXERCÍCIO 38', '-'*13)
print('=-'*20)
a = int(input('Digite dois números\n'))
b = int(input())
if a > b:
    print('O primeiro número é o maior.')
elif b > a:
    print('O segundo número é o maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
