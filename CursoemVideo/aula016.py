lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis. Ocorre erro na execução.
#Teste:
#lanche[1] = Refrigerante
print(lanche)
print(lanche[1:3]) #ignora o último
print(lanche[-1])
print(lanche[2:])
print(lanche[:2]) #ignora o último
print(lanche[-2:]) #não lê a tupla de trás para frente
for comida in lanche:
    print(comida)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche)) #imprime lanche organizado na ordem alfabética
