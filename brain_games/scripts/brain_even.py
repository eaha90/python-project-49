#!/usr/bin/env python3
from brain_games.games.game_even import game_even, QUESTION
from brain_games.engine import run_game


def main():
    run_game(game_even, QUESTION)


if __name__ == '__main__':
    main()
