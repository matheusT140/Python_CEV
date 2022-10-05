pessoa = {
    'nome': 'Matheus',
    'Idade': 26,
    'Sexo': 'M'
}
print(pessoa.values())
print(pessoa.keys())
print(pessoa.items())
for i, j in pessoa.items():
    print(f'{i}: {j}')
print(pessoa.keys(26))
