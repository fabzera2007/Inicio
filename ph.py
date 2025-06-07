print("---")
print("Verificador de pH")
print("---")

try:
    ph_str = input('Digite um valor de pH entre 0 e 14: ')
    ph = float(ph_str)

    if ph < 0 or ph > 14:
        print("Erro: O valor do pH deve ser entre 0 e 14.")
    elif ph > 7:
        print(f"O pH {ph:.1f} é: BÁSICO")
    elif ph < 7:
        print(f"O pH {ph:.1f} é: ÁCIDO")
    else: 
        print(f"O pH {ph:.1f} é: NEUTRO")

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número para o pH.")

print("---")
print("Verificação finalizada.")