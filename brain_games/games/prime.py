import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    root = int(number ** 0.5)
    possible_deviders = list(range(2, root + 1))
    for n in possible_deviders:
        if number % n == 0:
            return False
    return True


def get_random_number():
    return random.randint(1, 100)


def get_question_and_answer():
    number = get_random_number()
    answer = "yes" if is_prime(number) else "no"
    return str(number), answer
