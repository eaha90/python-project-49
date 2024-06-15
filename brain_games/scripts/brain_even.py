#!/usr/bin/env python3

from brain_games.game_engine import game_run
from brain_games.games import even


def main():
    game_run(even.GAME_DESCRIPTION)


if __name__ == "__main__":
    main()
