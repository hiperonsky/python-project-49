#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games import engine


def main():
    engine.engine(gcd.game, gcd.main_question)


if __name__ == '__main__':
    main()
