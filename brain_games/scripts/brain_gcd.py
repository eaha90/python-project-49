#!/usr/bin/env python3
from brain_games.games.gcd import gcd
from brain_games.engine import run_game


QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(gcd, QUESTION)


if __name__ == '__main__':
    main()
