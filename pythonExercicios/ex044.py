print('=-'*32)
print('-'*25, 'EXERCÍCIO 44', '-'*25)
print('-'*21, 'Cálculo de pagamento', '-'*21)
print('=-'*32)
print('Para o cálculo de pagamento deve-se especificar o preço do produto e forma de pagamento.')
p = float(input('Qual o preço normal do produto? '))
print('FORMAS DE PAGAMENTO: ')
print('[ 1 ] Dinheiro/cheque \n'
      '[ 2 ] À vista no cartão \n'
      '[ 3 ] 2x no cartão \n'
      '[ 4 ] 3x ou mais no cartão')
forma = int(input('Qual a forma de pagamento?'))
if forma == 1:
    print('Valor a ser pago: R${:.2f}.'.format(p*0.9))
elif forma == 2:
    print('Total a ser pago: R${:.2f}.'.format(p*0.95))
elif forma == 3:
    parcelas = p / 2
    print('Você pagará 2 parcelas de R${:.2f}.\n'
          'Total a ser pago: R${:.2f}'
          .format(parcelas, p))
else:
    n = int(input('Quantas parcelas?'))
    parcelas = (p*1.2) / n
    print('Você pagará {} parcelas de R${:.2f}.\n'
          'Total a ser pago: R${:.2f}'.format(n, parcelas, p*1.2))
