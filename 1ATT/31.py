#1014:

# Leitura eos valores de distância e combustível
dist = int(input('Qual a distância que será percorrida? = '))
comb = float(input('Quanto você gastou de Gasolina nesse trajeto? = '))

# Calc o consumo médio
consumo_medio = dist / comb

# Mostra o resultado com 3 casas decimais
print('{:.3f} km/l'.format(consumo_medio))