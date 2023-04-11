#!/usr/bin/env python3

import random
import prompt
from brain_games.cli import welcome_user, check, name


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        first_number = random.randint(0, 100)
        if first_number % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'
        print('Question: ' + str(first_number))
        user_answer = prompt.string('Your answer: ')
        if check(user_answer, true_answer) is False:
            break
        if i == 2:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
