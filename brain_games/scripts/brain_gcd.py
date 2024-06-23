#!/usr/bin/env python3
from brain_games.games.game_gcd import game_gcd, QUESTION
from brain_games.engine import run_game


def main():
    run_game(game_gcd, QUESTION)


if __name__ == '__main__':
    main()
