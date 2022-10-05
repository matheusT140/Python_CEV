from random import randint
print('{:=^31}'.format('Exercício 019'))
a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')
list = [a1, a2, a3, a4]
print('O aluno sorteado é: {}'.format(list[randint(0, 3)]))
