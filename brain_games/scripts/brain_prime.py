#!/usr/bin/env python3
from brain_games.games.game_prime import game_prime, QUESTION
from brain_games.engine import run_game


def main():
    run_game(game_prime, QUESTION)


if __name__ == '__main__':
    main()
