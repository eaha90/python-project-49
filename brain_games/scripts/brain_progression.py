#!/usr/bin/env python3

from brain_games.games import progression
from brain_games.scripts.game_engine import launch_game


def main():
    question, correct_answer = progression.generate_question()

    # name = input("May I have your name? ")
    # print(f"Hello, {name}!")

    try:
        launch_game(progression)
    except Exception as e:
        print(f"Error: {e}")

    if __name__ == "__main__":
        main()
