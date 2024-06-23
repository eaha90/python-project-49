from brain_games.cli import welcome_user
from .game import game


def main():
    print('Welcome to the Brain Games!')
    print(QUESTION)
    name = welcome_user()
    score = 0

    while score < 3:
        question, correct_answer = game()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if score == 3:
        print(f'Congratulations, {name}!')
