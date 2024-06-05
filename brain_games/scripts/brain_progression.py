#!/usr/bin/env python3

from brain_games.games import progression
from brain_games.scripts.game_engine import launch_game


def main():
    print(progression.GAME_DESCRIPTION)
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    launch_game(progression)

    if __name__ == "__main__":
        main()
