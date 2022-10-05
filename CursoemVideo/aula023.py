try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a/b
except(ValueError, TypeError):
    print('Ocorreu um problema com os tipos de dados digitados.')
except ZeroDivisionError:
    print('Não é possivel dividir por zero.')
except KeyboardInterrupt:
    print('Dados não informados.')
except Exception as erro:
    print(f'Ocorreu um erro: {erro.__cause__}')
else:
    print(f'O resultado é {c:.1f}')
finally:
    print('Encerrando programa... Volte sempre!')
