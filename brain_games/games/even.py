import random

DESCRIPTION = 'Answer "yes" if given number is prime or even. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_even(number):
    return number % 2 == 0


def get_question_and_answer(check_type):
    number = random.randint(1, 100)
    if check_type == 'prime':
        answer = "yes" if is_prime(number) else "no"
    elif check_type == 'even':
        answer = "yes" if is_even(number) else "no"
    else:
        raise ValueError("Unknown check type: {}".format(check_type))
    return str(number), answer
