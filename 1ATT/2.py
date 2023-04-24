#1040
#Valores:
n1, n2, n3, n4 = map(float, input('Insira suas notas = ').split())

#Média Ponderada:
mp = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

if mp >= 7.0:
    print(f"Media: {mp:.1f}\nAluno aprovado.")
elif mp < 5.0:
    print(f"Media: {mp:.1f}\nAluno reprovado.")
else:
    print(f"Media: {mp:.1f}\nAluno em exame.")
    exame = float(input())
    nova_media = (mp + exame) / 2
    print(f"Nota do exame: {exame:.1f}")
    if nova_media >= 5.0:
        print(f"Aluno aprovado.\nMedia final: {nova_media:.1f}")
    else:
        print(f"Aluno reprovado.\nMedia final: {nova_media:.1f}")
        