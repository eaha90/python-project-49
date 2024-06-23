import prompt
from brain_games.cli import welcome_user


def run_game(game_module):
    name = welcome_user()
    print(game_module.QUESTION)
    count = 0
    MAX_ROUNDS = 3

    while count < MAX_ROUNDS:
        question, correct_answer = game_module.game()
        print(f'Question: {question}')
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
