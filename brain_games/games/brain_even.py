#!/usr/bin/env python3

import random


def game():
    main_question = 'Answer "yes" if the number is even, otherwise answer "no".'
    first_number = random.randint(0, 100)
    question = 'Question: ' + str(first_number)
    if first_number % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return [main_question, question, true_answer]


def main():
    from brain_games.engine import engine
    engine()


if __name__ == '__main__':
    main()
