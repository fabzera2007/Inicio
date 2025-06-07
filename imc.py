try:
    mass_str = input('Digite seu peso em kg (ex: 75.5): ')
    mass = float(mass_str)

    height_str = input('Digite sua altura em metros (ex: 1.75): ')
    height = float(height_str)

    
    if height <= 0:
        print("Erro: A altura não pode ser zero ou um valor negativo. Por favor, insira uma altura válida.")
    else:
        imc = mass / (height ** 2)

       
        print(f"\nSeu IMC é: {imc:.2f}")

       
        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 24.9:
            print("Classificação: Peso normal")
        elif imc < 29.9:
            print("Classificação: Sobrepeso")
        elif imc < 34.9:
            print("Classificação: Obesidade Grau 1")
        elif imc < 39.9:
            print("Classificação: Obesidade Grau 2")
        else:
            print("Classificação: Obesidade Grau 3 (Mórbida)")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite apenas números para peso e altura.")

print("---")
