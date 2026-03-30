# Programa que calcula média e conceito do aluno

# Entrada das notas
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

# Cálculo da média
media = (n1 + n2 + n3 + n4) / 4

# Define conceito
if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

# Define situação
if conceito in ["A", "B", "C"]:
    status = "APROVADO"
else:
    status = "REPROVADO"

# Saída
print(f"Notas: {n1}, {n2}, {n3}, {n4}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {status}")
