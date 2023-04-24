#1006
# leitura das notas:

a = float(input('Digite aqui sua 1º nota = '))
b = float(input('Digite aqui sua 2º nota = '))
c = float(input('Digite aqui sua 3º nota = '))

# cálculo da média ponderada
media = (a*2 + b*3 + c*5)/10

# exibição do resultado com 1 casa decimal
print("MEDIA = {:.1f}".format(media))
