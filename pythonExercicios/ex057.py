print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 57', '-' * 34)
print('-' * 31, 'Leitura de gênero', '-' * 32)
print('=-' * 41)
genero = str(input('Digite seu sexo, masculino ou feminino (M/F): ')).upper()
while genero != 'M' and genero != 'F':
    print('Caractere não permitido. Digite "m" para masculino ou "f" para feminino.')
    genero = str(input()).upper()
if genero == 'M':
    print('Caractere válido. Você é do sexo masculino')
else:
    print('Caractere válido. Você é do sexo feminino')
