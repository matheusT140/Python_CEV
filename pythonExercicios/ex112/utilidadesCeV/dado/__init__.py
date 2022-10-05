def leiaDinheiro(s):
    n = str(input(s)).strip()
    if not n.isnumeric() or n == '':
        print(f'\033[0;31mERRO: "{n}" é um preço inválido!\033[m')
        return leiaDinheiro(s)
    return float(n.replace(',', '.'))
