# Inicializa a pontuação de cada casa
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

# Função para fazer uma pergunta e validar a entrada
def ask_question(question_text, options_dict, house_scores):
    """
    Exibe uma pergunta, coleta a resposta do usuário e atualiza as pontuações das casas.

    Args:
        question_text (str): O texto da pergunta.
        options_dict (dict): Um dicionário onde as chaves são os números das opções
                             e os valores são dicionários com 'text' (texto da opção)
                             e 'points' (dicionário de pontos para cada casa).
        house_scores (dict): O dicionário com as pontuações atuais das casas.
    
    Returns:
        bool: True se a resposta foi válida, False caso contrário.
    """
    print(f"\n{question_text}")
    for number, details in options_dict.items():
        print(f" {number}) {details['text']}")

    while True:
        try:
            answer = int(input(f'Digite sua resposta (1-{len(options_dict)}): '))
            if answer in options_dict:
                for house, points_to_add in options_dict[answer]['points'].items():
                    house_scores[house] += points_to_add
                return True
            else:
                print("Entrada inválida. Por favor, digite um número de opção válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Dicionários de perguntas para organizar o código
questions = [
    {
        "text": "Q1) Do you prefer Dawn or Dusk?",
        "options": {
            1: {"text": "Dawn", "points": {"gryffindor": 1, "ravenclaw": 1}},
            2: {"text": "Dusk", "points": {"hufflepuff": 1, "slytherin": 1}}
        }
    },
    {
        "text": "Q2) When I'm dead, I want people to remember me as:",
        "options": {
            1: {"text": "The Good", "points": {"hufflepuff": 2}},
            2: {"text": "The Great", "points": {"slytherin": 2}},
            3: {"text": "The Wise", "points": {"ravenclaw": 2}},
            4: {"text": "The Bold", "points": {"gryffindor": 2}}
        }
    },
    {
        "text": "Q3) Which kind of instrument most pleases your ear?",
        "options": {
            1: {"text": "The violin", "points": {"slytherin": 4}},
            2: {"text": "The trumpet", "points": {"hufflepuff": 4}},
            3: {"text": "The piano", "points": {"ravenclaw": 4}},
            4: {"text": "The drum", "points": {"gryffindor": 4}}
        }
    }
]

# Dicionário para armazenar as pontuações das casas
house_scores = {
    "gryffindor": 0,
    "hufflepuff": 0,
    "ravenclaw": 0,
    "slytherin": 0
}

# Loop através das perguntas e coleta as respostas
for q in questions:
    ask_question(q["text"], q["options"], house_scores)

print("\n--- Pontuação Final ---")
for house, score in house_scores.items():
    print(f"{house.capitalize()}: {score}")
print("-----------------------")

# Determina a casa com a maior pontuação
max_score = 0
sorted_house = ""

# Itera sobre as casas para encontrar a com a maior pontuação
# Se houver empate, a ordem aqui (Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
# determinará a casa "vencedora" em caso de pontuações iguais
if house_scores["gryffindor"] >= max(house_scores.values()):
    sorted_house = '🦁 Gryffindor!'
elif house_scores["ravenclaw"] >= max(house_scores.values()):
    sorted_house = '🦅 Ravenclaw!'
elif house_scores["hufflepuff"] >= max(house_scores.values()):
    sorted_house = '🦡 Hufflepuff!'
else: # Se não for nenhuma das anteriores com a maior pontuação, só pode ser Slytherin
    sorted_house = '🐍 Slytherin!'

print(f"\nParabéns! Você pertence à... {sorted_house}")
print("\n---")
print("Cálculo finalizado.")