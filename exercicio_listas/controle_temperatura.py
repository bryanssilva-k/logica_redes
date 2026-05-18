celsius = []

print("=== Controle de Temperaturas ===")
print("Digite temperaturas em Celsius (digite 'sair' para encerrar):")

while True:
    entrada = input("Temperatura (°C): ")
    if entrada.lower() == "sair":
        break
    try:
        temperatura = float(entrada)
        celsius.append(temperatura)
    except ValueError:
        print("Valor inválido. Digite um número ou 'sair'.")

if celsius:
    fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

    media_celsius = sum(celsius) / len(celsius)
    media_fahrenheit = sum(fahrenheit) / len(fahrenheit)

    print("\n=== Temperaturas Convertidas ===")
    print(f"{'Celsius':>10} | {'Fahrenheit':>10}")
    print("-" * 25)
    for c, f in zip(celsius, fahrenheit):
        print(f"{c:>9.1f}°C | {f:>9.1f}°F")

    print(f"\nMédia Celsius:    {media_celsius:.2f}°C")
    print(f"Média Fahrenheit: {media_fahrenheit:.2f}°F")
else:
    print("Nenhuma temperatura cadastrada.")
