print('=-'*32)
print('-'*25, 'EXERCÍCIO 43', '-'*25)
print('-'*24, 'Cálculo de IMC', '-'*24)
print('=-'*32)
print('Para o cálculo de índice de massa corporal, informe seu peso (KG): ')
p = float(input())
a = float(input('E a sua altura (m): '))
imc = p/(pow(a, 2))
if imc < 18.5:
    print('Você está abaixo do seu peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
