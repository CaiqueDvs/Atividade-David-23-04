#1010
# leitura dos dados da peça 1
cod_peca1, qtd_peca1, preco_peca1 = input('Valores peça 1 = ').split()
cod_peca1 = int(cod_peca1)
qtd_peca1 = int(qtd_peca1)
preco_peca1 = float(preco_peca1)

# leitura dos dados da peça 2
cod_peca2, qtd_peca2, preco_peca2 = input('Valores peça 2 = ').split()
cod_peca2 = int(cod_peca2)
qtd_peca2 = int(qtd_peca2)
preco_peca2 = float(preco_peca2)

# cálculo do valor total da compra
total = qtd_peca1 * preco_peca1 + qtd_peca2 * preco_peca2

# SAÍDA
print("VALOR A PAGAR: R$ {:.2f}".format(total))