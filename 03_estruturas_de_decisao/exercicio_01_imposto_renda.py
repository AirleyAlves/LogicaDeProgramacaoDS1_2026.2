"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario=float(input("digite o valor do seu salário: "))

#calculo dos numeros maior que 2000.00 e menor que 3000.00
taxa_1=(salario*0.08)
valor_taxa_1=(salario-taxa_1)

#calculo dos numeros maior que 3000.00 e menor que 4500.00
taxa_2=(salario*0.18)
valor_taxa_2=(salario-taxa_2)

#calculo dos numeros maior que 4500.00
taxa_3=(salario*0.28)
valor_taxa_3=(salario-taxa_3)

if salario<=2000.00:
    print("Isento")
elif 3000.00<salario>=2000.01 :
    print(f"o valor total foi R${valor_taxa_1:.2f}")
elif 4500.00<salario>3000.01 :
    print(f"o valor total foi R${valor_taxa_2:.2f}")
else:
    print(f"o valor total foi R${valor_taxa_3:.2f}")
