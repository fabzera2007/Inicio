
TAXA_DOLAR = 5.76 

PERCENTUAL_CALCULO = 0.17 

print("Calculadora de Reais")
print("---")

try:
    reais_str = input('Quantos reais você tem?: ')
    reais = int(reais_str)

   
    valor_percentual = reais * PERCENTUAL_CALCULO

   
    reais_em_dolar = reais / TAXA_DOLAR 

    print(f"\nCom R${reais:.2f} você tem:")
    print(f"- R${valor_percentual:.2f} (que é {PERCENTUAL_CALCULO:.0%} do valor inicial)")
    print(f"- Aproximadamente US${reais_em_dolar:.2f} (considerando a taxa de R${TAXA_DOLAR:.2f} por dólar)")

except ValueError:
    print("Erro: Por favor, digite um valor numérico válido para a quantidade de reais.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

print("---")
print("Cálculo finalizado.")