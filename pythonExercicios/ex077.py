print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 77', '-' * 34)
print('-' * 26, 'Mostrando as vogais da palavra', '-' * 24)
print('=-' * 41)
tupla = ('Aprender', 'Programar', 'Linguagem', 'Dinheiro', 'Sucesso',
         'Humildade', 'Disciplina', 'Comida', 'Atençao', 'Casa', 'Paralelepipedo',
         'Translucido', 'Onomatopeia')
for palavra in tupla:
    print(f'Na palavra {palavra.upper()} temos:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')
    print('')
