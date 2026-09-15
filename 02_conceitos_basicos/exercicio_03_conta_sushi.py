"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
#1.valor total consumido
total_consumido=float(input("qual o valor total consumido no restaurante ? "))
#2.taxa de 10% do garçom
taxa_garcom_porcentagem=float(10/100)
taxa_garcom_float=float(total_consumido*taxa_garcom_porcentagem)
#3.total da conta
total_conta=(total_consumido+taxa_garcom_float)
#4.mostrar
print(f"o total da conta ficou {total_conta}")