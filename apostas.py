import random

while True:
    print("DEVO APOSTAR? \n")

    numero_aleatorio = random.randint(1, 10)
    guess = 0
    tries = 0

    while guess != numero_aleatorio and tries < 2:
        try:
            guess = int(input('Fala um número ai de 1 a 10: '))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue 

        if guess < 1 or guess > 10:
            print("Número fora do intervalo. Por favor, digite um número entre 1 e 10.")
            continue
        
        tries += 1

    if guess != numero_aleatorio:
        print('Tá com azar hoje, nem tenta.')
        continuar = input('Quer tentar de novo? (s/n): ').lower()
        if continuar != 's':
            print("Programa encerrado.")
            break
    else:
        print('Vai na fé!')