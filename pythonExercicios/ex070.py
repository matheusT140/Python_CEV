print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 70', '-' * 34)
print('-' * 26, 'Programa Carrinho de Compras', '-' * 26)
print('=-' * 41)
total, prod1000mais, maisBarato = 0, 0, 0
nomeBarato = ''
while True:
    print('-' * 32)
    print('   LOJA SUPER BARATÃO   ')
    print('-' * 32)
    nome = str(input('Nome do Produto: ')).strip()
    preço = int(input('Preço: R$ '))
    if total == 0:
        maisBarato = preço
        nomeBarato = nome
    if preço < maisBarato:
        maisBarato = preço
        nomeBarato = nome
    if preço > 1000:
        prod1000mais += 1
    total += preço
    escolha = str(input('Quer continuar? [S/N] ')).lower()
    while escolha != 's' and escolha != 'n':
        escolha = str(input('Quer continuar? [S/N] ')).lower()
    if escolha == 'n':
        print(f' O total da compra foi R${total:.2f}')
        if prod1000mais == 0:
            print('Nenhum produto custa mais de R$1000.00')
        elif prod1000mais == 1:
            print('Temos um produto custando mais de R$1000.00')
        else:
            print(f'Temos {prod1000mais} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {nomeBarato} que custa R${maisBarato:.2f}')
        break
