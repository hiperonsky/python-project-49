#!/usr/bin/env python3

from brain_games.games import progression
from brain_games import engine


def main():
    engine.engine(progression.question_answer_generation,
                  progression.MAIN_QUESTION)


if __name__ == '__main__':
    main()
