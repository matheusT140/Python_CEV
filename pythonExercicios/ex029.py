print('--DETRAN traffic ticket calculator--')
s = float(input('Informe a velocidade do carro: '))
if s > 80:
    n = (s - 80)*7
    print('Veículo multado! Valor a pagar: {:.2f}.'.format(n))
else:
    print('Veículo em velocidade permitida.')
