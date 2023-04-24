#Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a
    #média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores
       # negativos e o percentual de valores negativos e positivos.
soma = 0
q_positivos = 0
q_negativos = 0

while True:
    valor = float(input('Digite um valor (ou 0 para sair): '))
    if valor <= 0:
        break
    
    soma += valor
    
    if valor > 0:
        q_positivos += 1
    else:
        q_negativos += 1

total_valores = q_positivos + q_negativos
media = soma / total_valores

perc_positivos = q_positivos / total_valores * 100
perc_negativos = q_negativos / total_valores * 100

print(f'A média aritmética dos valores é {media:.2f}.')
print(f'{q_positivos} valores são positivos ({perc_positivos:.2f}% do total).')
print(f'{q_negativos} valores são negativos ({perc_negativos:.2f}% do total).')

# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles
    #estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
        #terminar quando for lido um número negativo.
cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while True:
    num = float(input('Digite um número (ou um valor negativo para sair): '))
    if num < 0:
        break
    
    if 0 <= num <= 25:
        cont_0_25 += 1
    elif 26 <= num <= 50:
        cont_26_50 += 1
    elif 51 <= num <= 75:
        cont_51_75 += 1
    elif 76 <= num <= 100:
        cont_76_100 += 1

print(f'{cont_0_25} números estão no intervalo [0-25].')
print(f'{cont_26_50} números estão no intervalo [26-50].')
print(f'{cont_51_75} números estão no intervalo [51-75].')
print(f'{cont_76_100} números estão no intervalo [76-100].')
