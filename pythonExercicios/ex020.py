from random import sample
print('{:=^31}'.format('Exercício 020'))
a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')
lista = [a1, a2, a3, a4]
lista = sample(lista, k=len(lista))
print('A ordem da apresentação é: {}, {}, {} e {}.'.format(lista[0], lista[1], lista[2], lista[3]))
