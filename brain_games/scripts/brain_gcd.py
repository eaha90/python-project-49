# brain_games/scripts/brain_gcd.py

from brain_games.games import gcd
from brain_games.scripts.game_engine import launch_game


def main():
    launch_game(gcd)

if __name__ == "__main__":
    main()
