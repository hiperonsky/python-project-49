#!/usr/bin/env python3

import random
import prompt
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    general_counter = 0
    while general_counter < 3:
        first_number = random.randint(0, 100)
        if first_number % 2 == 0:
            true_answer = 'yes'
        else:
            true_answer = 'no'
        print('Question: ' + str(first_number))
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) != (true_answer):
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{str(true_answer)}'.")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
        general_counter += 1
        if general_counter == 3:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
