#!/usr/bin/env python3

from brain_games.game_engine import game_run
from brain_games.games import is_prime


def main():
    game_run(is_prime)


if __name__ == "__main__":
    main()
