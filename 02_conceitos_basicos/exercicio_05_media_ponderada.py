"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
#1.notas das avaliações
nota_1=float(input("qual foi a sua nota na primeira avaliação ? "))
nota_2=float(input("qual foi a sua nota na segunda avaliação ? "))
nota_3=float(input("qual foi a sua nota na terceira avaliação ? "))
#2.notas junto com o peso
peso_nota_1=(nota_1*2)
peso_nota_2=(nota_2*3)
peso_nota_3=(nota_3*5)
#3.média das notas
média_notas=(peso_nota_1+peso_nota_2+peso_nota_3/3)
#4.mostrar
print(f"a sua média é {média_notas}")