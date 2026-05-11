sistema_ligado = True

while sistema_ligado:

    try:
        temperatura = float(input("Digite a temperatura do servidor: "))

        if temperatura > 80:
            print("ALERTA: Resfriamento ativado")

        else:
            print("Temperatura normal")

    except ValueError:
        print("Erro: Digite um valor numérico válido.")

    resposta = input("Deseja continuar monitorando? (s/n): ")

    if resposta.lower() == "n":
        sistema_ligado = False

print("Sistema desligado")