#!/usr/bin/env python3
from brain_games.games.game_prime import game_prime
from brain_games.engine import run_game


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(game_prime, QUESTION)


if __name__ == '__main__':
    main()
