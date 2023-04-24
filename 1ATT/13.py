#  Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.
for i in range(101, 200, 2):
    print(i)
# Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N.
N = int(input("Digite um número de 1 a 10: "))

while N < 1 or N > 10:
    N = int(input("Valor inválido! Digite um número de 1 a 10: "))

for i in range(11):
    print(f"{i} x {N} = {i*N}")
    