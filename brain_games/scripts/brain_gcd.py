#!/usr/bin/env python3
from brain_games.games.game_gcd import game_gcd
from brain_games.engine import run_game


QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(game_gcd, QUESTION)


if __name__ == '__main__':
    main()
