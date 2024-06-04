from random import randint

GAME_DESCRIPTION = 'What is the result of the expression?'


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_question():
    operand1 = randint(1, 100)
    operand2 = randint(1, 100)
    operator = randint(1, 3)

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
