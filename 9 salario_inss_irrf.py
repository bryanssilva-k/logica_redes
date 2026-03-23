salario = float(input("Digite o salário: "))

# INSS (exemplo simplificado)
if salario <= 1320:
    inss = salario * 0.075
elif salario <= 2571:
    inss = salario * 0.09
else:
    inss = salario * 0.12

# IRRF (simplificado)
if salario <= 1903.98:
    irrf = 0
elif salario <= 2826.65:
    irrf = salario * 0.075
else:
    irrf = salario * 0.15

print(f"INSS: R$ {inss:.2f}")
print(f"IRRF: R$ {irrf:.2f}")