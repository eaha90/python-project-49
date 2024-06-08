import random

GAME_DESCRIPTION = 'What number is missing in this progression?'


def generate_question():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    progression_length = random.randint(5, 10)
    progression = [start + i * step for i in range(progression_length)]
    hidden_index = random.randint(0, progression_length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = f"Question: {' '.join(str(item) for item in progression)}"
    return question, correct_answer

ы
def get_user_answer():
    return input("Your answer: ")
