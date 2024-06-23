import random
import operator

QUESTION = 'What is the result of the expression?'


def game():
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operation = random.choice(list(operations.keys()))
    question = f'{number1} {operation} {number2}'
    correct_answer = str(operations[operation](number1, number2))    
    return question, correct_answer
