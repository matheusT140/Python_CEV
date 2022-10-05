nome = input('Digite o nome de uma cidade: ')
cidade = nome.split()
resp = 'santo' in cidade[0].lower()
print('A existência da palavra "Santo", no início do nome da cidade é: {}.'.format(resp))
