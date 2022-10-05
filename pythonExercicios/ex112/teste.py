from ex112.utilidadesCeV import moeda, dado
print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 112', '-' * 33)
print('-' * 27, 'Entrada de Dados Monetários', '-' * 26)
print('=-' * 41)
n = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(n, 10, 13)
