#!/usr/bin/env python3

from brain_games.games import calc
from brain_games import engine


def main():
    engine.run_game(calc.question_answer_generation, calc.MAIN_QUESTION)


if __name__ == '__main__':
    main()
