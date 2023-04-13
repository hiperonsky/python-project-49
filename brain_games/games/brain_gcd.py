#!/usr/bin/env python3

import random
from math import gcd


def game():
    main_question = 'Find the greatest common divisor of given numbers.'
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    true_answer = gcd(first_number, second_number)
    question = 'Question: ' + str(first_number) + ' ' + str(second_number)
    return [main_question, question, true_answer]


def main():
    from brain_games.engine import engine
    engine()


if __name__ == '__main__':
    main()
