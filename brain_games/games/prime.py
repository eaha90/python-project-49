import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(1, 100)

    def is_prime(number):
        if number == 1:
            return False
        root = int(number ** 0.5)
        possible_deviders = list(range(2, root + 1))
        for n in possible_deviders:
            if number % n == 0:
                return False
        return True
    answer = "yes" if is_prime(number) else "no"
    return str(number), answer
