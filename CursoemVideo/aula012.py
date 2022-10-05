nome = str(input('Qual é o seu nome? '))
print('Tenha um bom dia {}.'.format(nome))
if nome == 'Ana':
    print('Olá {}.'.format(nome))
elif nome == 'Ana': # Esta condição só é feita se somente a anterior for falsa.
                    # Dada a sua lógica ambígua a condição nunca será feita.
    print('Olá {}².'.format(nome))
else:
    print('Seja bem vindo.')
