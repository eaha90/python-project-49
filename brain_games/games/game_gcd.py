import random

MIN_NUMBER = 1
MAX_NUMBER = 100

QUESTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def game_gcd():
    random_int_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_int_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    result = gcd(random_int_1, random_int_2)
    question = f"{random_int_1} {random_int_2}"
    return question, str(result)
