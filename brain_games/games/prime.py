#!/usr/bin/env python3

import random


main_question = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def prime_number(number):
    if number <= 1:
        return 'no'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def game():
    number = random.randint(1, 100)
    true_answer = prime_number(number)
    question = str(number)
    return question, true_answer
