import prompt
from brain_games.cli import welcome_user


from brain_games.games.game_calc import game_calc, QUESTION as CALC_QUESTION
from brain_games.games.game_even import game_even, QUESTION as EVEN_QUESTION
from brain_games.games.game_gcd import game_gcd, QUESTION as GCD_QUESTION
from brain_games.games.game_prime import game_prime, QUESTION as PRIME_QUESTION
from brain_games.games.game_progression import game_progression, QUESTION as PROGRESSION_QUESTION


GAMES = {
    'calc': (game_calc, CALC_QUESTION),
    'even': (game_even, EVEN_QUESTION),
    'gcd': (game_gcd, GCD_QUESTION),
    'prime': (game_prime, PRIME_QUESTION),
    'progression': (game_progression, PROGRESSION_QUESTION),
}


def run_game(game_name):
    game, question = GAMES[game_name]
    name = welcome_user()
    print(question)
    count = 0
    MAX_ROUNDS = 3

    while count < MAX_ROUNDS:
        question, correct_answer = game()
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
