#!/usr/bin/env python3
from brain_games.engine import run_game
import brain_games.games.game_even as game_even


def main():
    run_game(game_even)

    if __name__ == '__main__':
        main()
