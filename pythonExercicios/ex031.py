print('Cálculo de passagem aérea')
d = int(input('Informe a distância do voo: '))
if d <= 200:
    v = d*0.5
else:
    v = d*0.45
print('Valor da passagem: R${:.2f}.'.format(v))
