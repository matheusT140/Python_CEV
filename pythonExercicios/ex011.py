print('{:=^31}'.format('Exercício 011'))
print('- Calculadora para quantidade necessária de tinta para pintura -')
w = int(input('Informe a largura e altura da parede a ser pintada.\nLargura(m): '))
h = int(input('Altura(m): '))
A = h*w
print('Serão necessários {} litros de tinta para realizar a pintura da parede.'.format((A/2)))
