print('--Cálculo de Salário--')
n = int(input('Informe o valor do seu salário: '))
if n > 1250:
    n2 = n * 1.1
else:
    n2 = n * 1.15
print('Salário inicial: R${:.2f}. Valor do salário com aumento: R${:.2f}. '.format(n, n2))
