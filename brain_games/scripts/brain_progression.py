#!/usr/bin/env python3

import random


def game():
    main_question = 'What number is missing in the progression?'
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
    question = 'Question: ' + " ".join(map(str, list))
    return [main_question, question, true_answer]


def main():
    from brain_games.engine import engine
    engine()


if __name__ == '__main__':
    main()
