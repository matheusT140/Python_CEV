print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 100', '-' * 33)
print('-' * 24, 'Função - Obrigatoriedade de Voto', '-' * 24)
print('=-' * 41)


def voto(year):
    from datetime import date
    anos = date.today().year - year
    if anos >= 16:
        if anos < 18 or anos > 70:
            print(f'Com {anos} anos: VOTO OPCIONAL.')
        else:
            print(f'Com {anos} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {anos} anos: NÃO VOTA.')


voto((int(input('Em que ano você nasceu? '))))
