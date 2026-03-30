n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("1-Adição 2-Subtração 3-Multiplicação 4-Divisão")
print("5-Potência 6-Raiz quadrada 7-Par 8-Ímpar")

op = int(input("Escolha: "))

if op == 1:
    print(n1 + n2)
elif op == 2:
    print(n1 - n2)
elif op == 3:
    print(n1 * n2)
elif op == 4:
    print(n1 / n2)
elif op == 5:
    print(n1 ** n2)
elif op == 6:
    print(n1 ** 0.5, n2 ** 0.5)
elif op == 7:
    print("Par" if n1 % 2 == 0 else "Ímpar")
elif op == 8:
    print("Ímpar" if n1 % 2 != 0 else "Par")
else:
    print("Opção inválida")
