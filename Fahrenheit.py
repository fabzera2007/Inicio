MULTIPLICACAO = 1.8
ADICAO = 32

print("---")
print("Conversor de Temperatura: Celsius para Fahrenheit")
print("---")

try:
    celsius_str = input('Qual a temperatura em Celsius?: ')
    celsius = float(celsius_str) 

    fahrenheit = (celsius * MULTIPLICACAO) + ADICAO

    print(f"\n{celsius:.1f}°C equivalem a {fahrenheit:.1f}°F.")

except ValueError:
    print("Erro: Por favor, digite um valor numérico válido para a temperatura.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

print("---")
print("Conversão finalizada.")