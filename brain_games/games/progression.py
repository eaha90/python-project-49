import random

GAME_DESCRIPTION = "What number is missing in the progression?"


def generate_progression(length, step):

    start = random.randint(1, 50)
    progression = [start + i * step for i in range(length)]
    return progression


def generate_question():

    length = random.randint(5, 10)
    step = random.randint(1, 10)
    progression = generate_progression(length, step)

    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = ".."

    question = ' '.join(str(x) for x in progression)
    correct_answer = str(hidden_value)
    return question, correct_answer
