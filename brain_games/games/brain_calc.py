#!/usr/bin/env python3

import random


def game():
    main_question = 'What is the result of the expression?'
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    oper_number = random.randint(1, 3)
    if oper_number == 1:
        true_answer = first_number + second_number
        exp_char = '+'
    elif oper_number == 2:
        true_answer = first_number - second_number
        exp_char = '-'
    else:
        true_answer = first_number * second_number
        exp_char = '*'
    question = f"Question: {str(first_number)} {exp_char} {str(second_number)}"
    return [main_question, question, true_answer]


def main():
    from brain_games.engine import engine
    engine()


if __name__ == '__main__':
    main()
