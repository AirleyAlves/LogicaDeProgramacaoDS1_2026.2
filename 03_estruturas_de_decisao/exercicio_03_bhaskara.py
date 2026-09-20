"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
import math
a=float(input("digite o valor do a da sua função: "))
b=float(input("digite o valor do b da sua função: "))
c=float(input("digite o valor do c da sua função: "))
delta=(b*b)-4*a*c
if delta>0:
    raiz_de_delta=math.sqrt(delta)
    raiz_x1=(-b+raiz_de_delta)/2*a
    raiz_x2=(-b-raiz_de_delta)/2*a
    print(f"as raizes da sua função é {raiz_x1:.5f} e {raiz_x2:.5f}")
else:
    print("impossivel calcular")



