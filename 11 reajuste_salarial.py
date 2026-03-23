salario = float(input("Digite o salário: "))

if salario <= 1000:
    percentual = 0.20
elif salario <= 1700:
    percentual = 0.15
elif salario <= 2300:
    percentual = 0.10
else:
    percentual = 0.05

aumento = salario * percentual
novo = salario + aumento

print(f"Salário antigo: R$ {salario:.2f}")
print(f"Aumento: {percentual*100}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo:.2f}")