#!/usr/bin/env python3

import prompt


def engine(game, main_question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(main_question)
    for i in range(3):
        question, true_answer = game()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) != str(true_answer):
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{str(true_answer)}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
    print('Congratulations, ' + name + '!')


def main():
    engine()


if __name__ == '__main__':
    main()
