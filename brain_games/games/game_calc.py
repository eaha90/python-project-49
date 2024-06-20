import random

MIN_NUMBER = 1
MAX_NUMBER = 10


def game_calc():
    random_int_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_int_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    action = random.choice(['*', '+', '-'])
    
    if action == '+':
        result = random_int_1 + random_int_2
    elif action == '-':
        result = random_int_1 - random_int_2
    elif action == '*':
        result = random_int_1 * random_int_2
    
    operation = f'{random_int_1} {action} {random_int_2}'
    return operation, result
