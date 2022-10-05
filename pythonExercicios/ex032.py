print('--Calculadora de ano bissexto--')
y = int(input('Informe o ano: '))
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print('O ano é bissexto.')
        else:
            print('O ano não é bissexto.')
    else:
        print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')
    