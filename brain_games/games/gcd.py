import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f"{first_number} {second_number}"
    answer = str(math.gcd(first_number, second_number))
    return question, answer
