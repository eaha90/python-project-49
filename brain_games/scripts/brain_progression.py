# brain_games/scripts/brain_progression.py

from brain_games.games import progression
from brain_games.scripts.game_engine import launch_game


def main():
    print(progression.GAME_DESCRIPTION)
    launch_game(progression)

if __name__ == "__main__":
    main()
