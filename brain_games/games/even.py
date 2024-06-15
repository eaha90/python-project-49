import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return False if number % 2 else True


def get_question_and_answer():
    number = random.randint(1, 100)
    answer = "yes" if is_even(number) else "no"
    return str(number), answer
