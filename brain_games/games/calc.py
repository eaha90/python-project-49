import random

GAME_DESCRIPTION = "What is the result of the expression?"  # Описание игры


def generate_question():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 20)
    operation = random.choice(operations)
    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(question))
    return question, correct_answer
