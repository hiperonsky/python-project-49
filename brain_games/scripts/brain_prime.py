#!/usr/bin/env python3

import random


def prime_number(number):
    if number <= 1:
        return 'no'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def game():
    main_question = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
    number = random.randint(1, 100)
    true_answer = prime_number(number)
    question = 'Question: ' + str(number)
    return [main_question, question, true_answer]


def main():
    from brain_games.engine import engine
    engine()


if __name__ == '__main__':
    main()
