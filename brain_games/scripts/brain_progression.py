#!/usr/bin/env python3
from brain_games.games.progression import progression
from brain_games.engine import run_game


QUESTION = 'What number is missing in the progression?'


def main():
    run_game(progression, QUESTION)


if __name__ == '__main__':
    main()
