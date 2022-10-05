nome = input('Digite um nome: ')
nome = nome.lower()
nome = nome.split()
resp = 'silva' in nome
print('A existência de "Silva" no nome é: {}.'.format(resp))
