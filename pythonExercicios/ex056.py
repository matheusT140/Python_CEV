print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 56', '-' * 34)
print('-' * 31, 'Programa de idade', '-' * 32)
print('=-' * 41)
idade = []
nome = []
sexo = []
mnVinte = 0
media = 0
maisVelho = 0
for i in range(0, 4):
    nome += [str(input('Digite o nome da {} pessoa: '.format(i + 1)))]
    idade += [int(input('Sua idade: '))]
    sexo += [str(input('Seu sexo (M/F): '))]
    if idade[i] > maisVelho and sexo[i] == 'Mm': # 'Mm' para ler tanto maiúsculo quanto minúsculo
        maisVelho = i
    if sexo[i] == 'Ff' and idade[i] < 20: # 'Ff' para ler tanto maiúsculo quanto minúsculo
        mnVinte += 1
    media += idade[i]
print('A média de idade do grupo é de {:.2f} anos.'.format(media/4))
print('O homem mais velho do grupo é {}.'.format(nome[maisVelho]))
if mnVinte == 0:
    print('Não há mulheres com menos de 20 anos no grupo.')
elif mnVinte == 1:
    print('Há uma mulher com menos de 20 anos no grupo.')
else:
    print('Há {} mulheres com menos de 20 anos no grupo.')
