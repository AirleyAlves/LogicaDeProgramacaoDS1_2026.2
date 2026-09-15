"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
#1. qual é a distância percorrida em km
distancia_km=float(input("qual foi a distância percorrida ? "))
#2. qual o total de combustivel gasto
combustivel_gasto=float(input("quanto de combustivel foi gasto ? "))
#3. quanto de combustivel por quilometros
combustivel_por_km=(distancia_km/combustivel_gasto)
#4 mostrar
print(f"foram ultilizados {combustivel_por_km} litros de combustivel por quilometros.")
#fim