def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau I"
    elif imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"


while True:
    try:
        print("\n=== Cálculo de IMC ===")
        print("Digite -1 no peso para encerrar.")
        peso = float(input("Informe seu peso (kg): "))
        if peso == -1:
            print("Encerrando o programa. Até logo!")
            break  # sai do loop
        altura = float(input("Informe sua altura (m): "))
        if peso <= 0 or altura <= 0:
            print("Erro: valores de peso e altura devem ser positivos!")
            continue
        imc = calcular_imc(peso, altura)
        situacao = classificar_imc(imc)
        print(f"\nSeu IMC é {imc:.2f}")
        print(f"Situação: {situacao}")
    except ValueError:
        print("Entrada inválida! Por favor, digite valores numéricos.")
