#!/usr/bin/env python3

from brain_games.games import calc
from brain_games import engine


def main():
    engine.engine(calc.game, calc.MAIN_QUESTION)


if __name__ == '__main__':
    main()
