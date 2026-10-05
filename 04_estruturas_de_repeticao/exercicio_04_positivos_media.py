"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
lista=[]
soma=0
for i in range(6):
    numero=int(input("digite um numero "))
    if numero > 0:
        lista.append(numero)
        media= sum(lista) / len(lista)
        contador= len(lista)


print(f"a quantidade dos numeros positivos é {contador}")
print(f"a média dos numeros positivos digitados é {media:.1f}")