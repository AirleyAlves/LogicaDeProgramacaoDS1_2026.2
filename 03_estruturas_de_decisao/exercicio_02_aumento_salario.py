"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario=float(input("digite o valor do seu salário: "))
#taxa de aumento de salário: de 0.00 até 400.00
taxa_01=(salario*0.15)
salario_taxa_01=(salario+taxa_01)
#taxa de aumento de salário: de 400.01 até 800.00
taxa_02=(salario*0.12)
salario_taxa_02=(salario+taxa_02)
#taxa de aumento de salário: de 800.01 até 1200.00
taxa_03=(salario*0.10)
salario_taxa_03=(salario+taxa_03)
#taxa de aumento de salário: de 1200.01 até 2000.00
taxa_04=(salario*0.07)
salario_taxa_04=(salario+taxa_04)
#taxa de aumento de salário: acima de 2000.00
taxa_05=(salario*0.04)
salario_taxa_05=(salario+taxa_05)
if 0.00<salario<=400.00:
    print(f"o seu novo salário é R${salario_taxa_01:.2f}")
elif 400.00<salario<=800.00:
    print(f"o seu novo salário é R${salario_taxa_02:.2f}")
elif 800.00<salario<=1200.00:
    print(f"o seu novo salário é R${salario_taxa_03:.2f}")
elif 1200.00<salario<=2000.00:
    print(f"o seu novo salário é R${salario_taxa_04:.2f}")
else:
    print(f"o seu novo salário é R${salario_taxa_05:.2f}")