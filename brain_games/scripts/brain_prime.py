#!/usr/bin/env python3

from brain_games.games import prime
from brain_games import engine


def main():
    engine.run_game(prime.question_answer_generation, prime.MAIN_QUESTION)


if __name__ == '__main__':
    main()
