# Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
A = int(input("Digite um número inteiro para calcular o seu fatorial, painhooo =   "))

fatorial = 1

print(f"{A}! = ", end="")

for i in range(A, 0, -1):
    fatorial *= i
    print(i, end="")
    if i != 1:
        print(" X ", end="")
    else:
        print(" = ", end="")
        
print(fatorial)
