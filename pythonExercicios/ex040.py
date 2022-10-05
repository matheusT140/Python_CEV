print('=-'*20)
print('-'*13, 'EXERCÍCIO 40', '-'*13)
print('-'*11, 'Programa de notas', '-'*10)
print('=-'*20)
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Agora a segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('REPROVADO')
elif 4.9 < m < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
