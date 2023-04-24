#1015:
    # LEMBRETE
    # Distancia = SQRT (X2 -X1)**2 + (Y2 - Y1)**2

x1, y1 = map(float, input('Insira seus eixos primários = ').split())
x2, y2 = map(float, input('Insira seus exios secundários = ').split())

distancia = mh.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print('{:.4f}'.format(distancia))