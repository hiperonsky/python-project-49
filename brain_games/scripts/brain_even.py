#!/usr/bin/env python3

# from brain_games.games import brain_even

from brain_games.games import even
from brain_games import engine


def main():
    engine.engine(even.game, even.main_question)


if __name__ == '__main__':
    main()
