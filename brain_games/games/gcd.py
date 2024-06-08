import random

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    gcd = 1
    for i in range(1, min(number1, number2) + 1):
        if number1 % i == 0 and number2 % i == 0:
            gcd = i

    return f"{number1} {number2}", str(gcd)
