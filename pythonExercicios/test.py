sequencia = []
sequencia += [1]
sequencia += [1]
sequencia += [2]
sequencia[0] = sequencia[1] + sequencia[2]
sequencia[1] = sequencia[0] + sequencia[2]
sequencia[2] = sequencia[0] + sequencia[1]
print(sequencia)
