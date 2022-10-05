ex = 'Exercício 008'
print('{:=^30}' .format(ex))
n = int(input('Calculadora de conversão. Metros para centímetros e milímetros.\nInsira a metragem: '))
print('Conversão:\n{} m = {} cm. \n{} m = {} mm.' .format(n, (n*100), n, (n*1000)))
