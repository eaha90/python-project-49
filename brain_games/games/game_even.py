import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def game_even():
    random_int = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if random_int % 2 == 0 else 'no'
    return random_int, correct_answer
