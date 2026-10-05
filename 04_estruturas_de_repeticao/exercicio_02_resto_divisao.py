"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
x=int(input("digite um numero: "))
y=int(input("digite outro numero: "))

inicio=min(x,y)+1
fim=max(x,y)

for seq in range(inicio,fim):
    if seq%5 == 2 or seq%5 == 3 :
        print(seq)

