# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.G contendo 10 valores
A = float(input("Digite o valor inicial da P.G.: "))
R = float(input("Digite a razão da P.G.: "))

for i in range(10):
    print(A)
    A *= R