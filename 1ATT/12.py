#  Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.
    #Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. 
    # O número que encerrará a leitura será zero.
numeros = []
numero = int(input('Digite um número: '))
while numero != 0:
    numeros.append(numero)
    numero = int(input('Digite um número: '))

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 == 1]

media_pares = sum(pares) / len(pares) if len(pares) > 0 else 0
media_geral = sum(numeros) / len(numeros) if len(numeros) > 0 else 0

print(f'Números pares: {len(pares)}')
print(f'Números ímpares: {len(impares)}')
print(f'Média dos números pares: {media_pares:.2f}')
print(f'Média geral dos números: {media_geral:.2f}')