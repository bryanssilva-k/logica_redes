# Programa que verifica se três lados formam um triângulo

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# Verifica se pode formar um triângulo
if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não forma um triângulo")
