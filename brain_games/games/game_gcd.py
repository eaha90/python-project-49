import random
import math

def game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f'Question: {number1} {number2}'
    correct_answer = str(math.gcd(number1, number2))
    return question, correct_answer
