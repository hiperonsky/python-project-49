#!/usr/bin/env python3

import prompt
from brain_games.games.brain_even import game
from brain_games.games.brain_gcd import game
from brain_games.games.brain_calc import game
from brain_games.games.brain_prime import game
from brain_games.games.brain_progression import game


def engine():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game()[0])
    for i in range(0, 3):
        [main_question, question, true_answer] = game()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) != str(true_answer):
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{str(true_answer)}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        if i == 2:
            print('Congratulations, ' + name + '!')


def main():
    engine()


if __name__ == '__main__':
    main()
