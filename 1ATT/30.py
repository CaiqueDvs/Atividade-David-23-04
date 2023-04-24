#1012
# Leitura dos valores de entrada:
a, b, c = map(float, input('Insira aqui seus respectivos valores de entrada A, B e C = ').split())

# Cálculo das áreas:
    #LEMBRETE ------->
        #a) a área do triângulo retângulo que tem A por base e C por altura.
        #b) a área do círculo de raio C. (pi = 3.14159)
        #c) a área do trapézio que tem A e B por bases e C por altura.
        #d) a área do quadrado que tem lado B.
        #e) a área do retângulo que tem lados A e B.
#Cálculo:
triangulo = (a * c) / 2
circulo = mh.pi * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b ** 2
retangulo = a * b

# Impressão dos resultados das Formas:
print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))

#1013

a, b, c = input('Insira seus Valores para cálculo =  ').split() # Leitura dos Valores como str
a, b, c = int(a), int(b), int(c) # Conversão de str 

maior_ab = (a + b + abs(a - b)) / 2 # Calculo do Maior valor 
maior_abc = (maior_ab + c + abs(maior_ab - c)) / 2 #Calculo do Maior Valor entre o antecessor e o valor de C

print(f"{maior_abc} EH o maior") #Saída