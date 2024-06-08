import random
import prompt

GAME_DESCRIPTION = 'Answer "yes" if the number is prime. Otherwise answer "no".'


def generate_question():
    number = random.randint(1, 100)
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    correct_answer = 'yes' if is_prime else 'no'
    return str(number), correct_answer
