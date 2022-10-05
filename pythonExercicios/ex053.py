print('=-' * 41)
print('-' * 34, 'EXERCÍCIO 53', '-' * 34)
print('-' * 27, 'Verificador de palíndromo', '-' * 28)
print('=-' * 41)
frase = str(input('Digite uma frase: '))
esarf = ''
frase = frase.lower().strip().split()
frase2 = ''.join(frase) # pega frase já em split e junta toda em frase2
#depois é só inverter:
for i in range(0, len(frase2)):
    esarf += frase2[len(frase2)-(i+1)]
if frase2 == esarf:
    print('Palíndromo detectado!')
else:
    print('A frase ou palavra não é um palíndromo')
