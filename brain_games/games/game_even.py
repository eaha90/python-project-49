import random

MIN_NUMBER = 1
MAX_NUMBER = 100

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    random_int = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{random_int}'
    correct_answer = 'yes' if random_int % 2 == 0 else 'no'
    return question, correct_answer
