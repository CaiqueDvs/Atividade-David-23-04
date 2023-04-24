# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.A contendo valores 10 valores.
A = float(input("Digite o valor inicial da P.A.: "))
R = float(input("Digite a razão da P.A.: "))

for i in range(10):
    print(A)
    A += R