print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 65', '-' * 34)
print('-' * 29, 'Leitura de Vários Números 2', '-' * 29)
print('=-' * 41)
maior, menor, media, contador = 0, 0, 0, 0
res = 's'
while res == 's':
    n = int(input('Digite um número: '))
    if contador == 0:
        menor = n
    contador += 1
    media += n
    if maior < n:
        maior = n
    elif menor > n:
        menor = n
    res = str(input('Deseja continuar (S/N)?')).lower()
media = media/contador
print('Média dos números digitados: {}.\nMaior número digitado: {}.\n'
      'Menor número: {}.'.format(media, maior, menor))
