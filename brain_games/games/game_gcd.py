import prompt
from brain_games.cli import welcome_user
from random import randint
import math

QUESTION = 'Find the greatest common divisor of given numbers.'


def game_gcd():
    random_int_1 = randint(1, 100)
    random_int_2 = randint(1, 100)
    question = f"{random_int_1} {random_int_2}"
    correct_answer = math.gcd(random_int_1, random_int_2)
    return question, correct_answer


def run_game(game_module):
    name = welcome_user()
    count = 0
    MAX_ROUNDS = 3

    while count < MAX_ROUNDS:
        question, correct_answer = game_module.game()
        print(f'Question: {QUESTION} {question}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;( "
                  + f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    if count == MAX_ROUNDS:
        print(f'Congratulations, {name}!')
