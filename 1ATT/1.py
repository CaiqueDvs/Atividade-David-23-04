#1038
codigo, quantidade = map(int, input('Insira aqui o que você deseja adquirir 1.Cachorro Quente - 2.X-Salada -  3.X-Bacon - 4.Torrada 5.Refrigerante ').split())

if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50

total = preco * quantidade

print("Total: R$ {:.2f}".format(total))
