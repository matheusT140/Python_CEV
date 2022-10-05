from random import randint
n = randint(0, 5)
print('Desafio. Tente adivinhar qual número a máquina "pensou", entre 0 e 5.')
n2 = int(input('Seu palpite?'))
if n2 == n:
    print('Boa, Você acertou!')
else:
    print('Ih, não é seu dia de sorte meu chapa :/.')
