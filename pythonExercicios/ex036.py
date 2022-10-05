print('=-'*20)
print(' '*8, 'MATHEUS EMPRÉSTIMOS')
print('=-'*20)
c = int(input('Informe o valor da casa para o empréstimo destinado.\n'))
s = int(input('Agora informe o seu salário\n'))
a = int(input('Em quantos anos se pretende pagar o valor da casa? (até 50 anos s/juros)\n'))
p = c/(a*12)

if a <= 50:
    if p <= (s*0.3):
        print('Empréstimo aprovado. Você pagará R${} mensalmente, pelos próximos {} anos.'.format(p, a))
        input()
    elif a == 50 and p > (s*0.3):
        print('O valor da parcela excede o limite de 30% do salário.')
        input()
    elif a < 50:
        print('O valor da parcela excede o limite de 30% do salário.\nTente com quantidades de parcelas menores')
        input()
else:
    print('Para parcelas acima de 50 anos será cobrada uma taxa de juros.')
