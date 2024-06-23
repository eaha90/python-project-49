#!/usr/bin/env python3
from brain_games.games.game_calc import game_calc, QUESTION
from brain_games.engine import run_game


def main():
    run_game(game_calc, QUESTION)


if __name__ == '__main__':
    main()
