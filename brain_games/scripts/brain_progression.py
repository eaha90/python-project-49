#!/usr/bin/env python3
from brain_games.games.game_progression import game_progression, QUESTION
from brain_games.engine import run_game


def main():
    run_game(game_progression, QUESTION)


if __name__ == '__main__':
    main()
