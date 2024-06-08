import random

GAME_DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operator = random.randint(1, 3)

    if operator == 1:
        expression = f"{operand1} + {operand2}"
        correct_answer = str(operand1 + operand2)
    elif operator == 2:
        expression = f"{operand1} - {operand2}"
        correct_answer = str(operand1 - operand2)
    else:
        expression = f"{operand1} * {operand2}"
        correct_answer = str(operand1 * operand2)

    return expression, correct_answer
