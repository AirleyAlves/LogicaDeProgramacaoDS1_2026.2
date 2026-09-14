# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
valor_conta_str=input("quanto deu a conta ? ")
valor_conta=float(valor_conta_str)
# 2. Leia o número de pessoas (int)
numero_de_pessoas_str=input("quantas pessoas estão ? ")
numero_de_pessoas=int(numero_de_pessoas_str)
# 3. Calcule o valor por pessoa
valor_individual=(valor_conta/numero_de_pessoas)
valor_individal_str=str(valor_individual)
# 4. Imprima formatado usando f-string
print(f"será pago {valor_individual} reais por cada um")
#5.fim