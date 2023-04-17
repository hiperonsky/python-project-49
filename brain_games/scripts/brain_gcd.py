#!/usr/bin/env python3

from brain_games.games import gcd
from brain_games import engine


def main():
    engine.engine(gcd.question_answer_generation, gcd.MAIN_QUESTION)


if __name__ == '__main__':
    main()
