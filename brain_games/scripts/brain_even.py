#!/usr/bin/env python3

from brain_games.cli import print_rules
from brain_games.games import even


def main():
    print_rules(even.RULES)

if __name__ == "__main__":
    main()
