#!/usr/bin/env python3


from brain_games.games import even
from brain_games import engine


def main():
    engine.run_game(even.question_answer_generation, even.MAIN_QUESTION)


if __name__ == '__main__':
    main()
