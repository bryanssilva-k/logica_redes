a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

# Verifica se forma triângulo
if a + b > c and a + c > b and b + c > a:
    print("Forma um triângulo!")

    if a == b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não forma um triângulo!")