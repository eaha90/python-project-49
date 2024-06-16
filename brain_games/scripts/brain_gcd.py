#!/usr/bin/env python3
from brain_games.games.generate_gcd_problem import generate_gcd_problem
from brain_games.engine import run_game


QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(generate_gcd_problem, QUESTION)


if __name__ == '__main__':
    main()
