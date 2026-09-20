# TODO: Implemente a expressão de validação
media_aluno = float(input("qual foi a média do aluno ?" ))
frequencia_percentual = float(input("qual foi a frequencia porcentual do aluno ? "))

# Crie a variável aprovado com a expressão lógica
aprovado = (media_aluno>=6 and frequencia_percentual>=75)
print("status de aprovação:", aprovado)
