import random

GAME_DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."  # Описание игры

def generate_question():
    number = random.randint(1, 100)
    question = f"Question: {number}"
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer
