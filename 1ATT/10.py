# Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500:
soma = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i

print(soma)
# Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar:
    #A. Menor Altura;
    #B. Menor Altura;
meh = float('inf')
mah = float('-inf')

for i in range(15):
    altura = float(input(f'Digite aqui a altura da {i+1}ª pessoa: '))
    if altura < meh:
        meh = altura
    if altura > mah:
        mah = altura
1
print(f'A menor altura do grupo é {meh:.2f} m.')
print(f'A maior altura do grupo é {mah:.2f} m.')