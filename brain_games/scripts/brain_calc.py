#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.calc import calc


QUESTION = 'What is the result of the expression?'


def main():
    run_game(calc, QUESTION)


if __name__ == '__main__':
    main()
