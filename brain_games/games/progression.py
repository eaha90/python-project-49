from random import randint

GAME_DESCRIPTION = 'What number is missing in this progression?'


def welcome_user():

    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_question():

    start = randint(1, 10)
    step = randint(1, 10)
    progression_length = randint(5, 10)
    hidden_index = randint(0, progression_length - 1)
    progression = [start + i * step for i in range(progression_length)]
    progression[hidden_index] = ".."
    correct_answer = str(start + hidden_index * step)
    return " ".join(str(x) for x in progression), correct_answer
