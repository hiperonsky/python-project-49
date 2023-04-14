#!/usr/bin/env python3

import random


main_question = 'What number is missing in the progression?'


def game():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 12)
    counter = 0
    list = []
    while counter < 10:
        list.append(first_number)
        first_number = first_number + second_number
        counter += 1
    prog_random_position = random.randint(0, 9)
    true_answer = list[prog_random_position]
    list[prog_random_position] = '..'
    question = " ".join(map(str, list))
    return question, true_answer
