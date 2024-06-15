from random import randint
import math

DESCRIPTION = 'Answer "yes" if the number is prime. Otherwise answer "no".'


def is_prime(num):
    mx = math.sqrt(num)

    i = 2
    while i <= mx:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def run_game():
    question = randint(0, 100)
    prime = 'yes' if is_prime(question) else 'no'

    return (question, prime)
