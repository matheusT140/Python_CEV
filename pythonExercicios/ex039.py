from datetime import date
print('=-'*20)
print('-'*13, 'EXERCÍCIO 39', '-'*13)
print('=-'*20)
print('informe sua data de nascimento: ')
d = int(input('Dia: '))
m = int(input('Mês: '))
a = int(input('Ano: '))
btd = date(a, m, d)
today = date.today()
if today.year-btd.year < 18:
    enlistment_date = today.replace(year=(today.year+(18-(today.year-btd.year))), day=1, month=1)
    if enlistment_date.year-today.year >= 1:
        if enlistment_date.year-today.year > 1:
            print('Faltam {} anos para você se alistar.'.format(enlistment_date.year - today.year))
        else:
            print('Falta {} ano para você se alistar.'.format(enlistment_date.year - today.year))
    else:
        print('Faltam {} dias para você se alistar.'.format((enlistment_date-today).days))
elif today.year-btd.year > 18:
    past_enlistment_date = btd.replace(year=(today.year-((today.year-btd.year)-18)), day=1, month=1)
    if today.year - past_enlistment_date.year >= 1:
        if today.year - past_enlistment_date.year == 1:
            print('Você tem mais de 18 anos. Seu alistamento foi a {} ano atrás.'.format(
                today.year - past_enlistment_date.year))
        else:
            print('Você tem mais de 18 anos. Seu alistamento foi a {} anos atrás.'
                  .format(today.year-past_enlistment_date.year))
    else:
        # today - past_enlistment_date # retorna o tempo
        # passado entre as datas em formato de dia e hora especifica
        print('Você tem mais de 18 anos. Seu alistamento foi a {} dias atrás.'.format((today-past_enlistment_date).days))
else:
    print('Nesse ano você completará 18 anos, portanto você deve se alistar.')
