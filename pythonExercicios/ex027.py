nome = str(input('Digite o seu nome completo: ')).strip()
nome2 = nome.split()
print('Primeiro nome: {}'.format(nome2[0]))
print('Último nome: {}'.format(nome2[len(nome2)-1]))
