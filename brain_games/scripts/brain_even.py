#!/usr/bin/env python3

import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    first_number = random.randint(0, 100)
    if first_number % 2 == 0:
        first_true_answer = 'yes'
    else:
        first_true_answer = 'no'
    second_number = random.randint(0, 100)
    if second_number % 2 == 0:
        second_true_answer = 'yes'
    else:
        second_true_answer = 'no'
    third_number = random.randint(0, 100)
    if third_number % 2 == 0:
        third_true_answer = 'yes'
    else:
        third_true_answer = 'no'
    
    print('Question: ' + str(first_number))
    first_answer = prompt.string('Your answer: ')
    if first_answer != first_true_answer:
        print("'" + first_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + first_true_answer + "'.")
        print("Let's try again, " + name + "!")
    else:
        print('Correct!')
        print('Question: ' + str(second_number))
        second_answer = prompt.string('Your answer: ')
        if second_answer != second_true_answer:
            print("'" + second_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + second_true_answer + "'.")
            print("Let's try again, " + name + "!")
        else:
            print('Correct!')
            print('Question: ' + str(third_number))
            third_answer = prompt.string('Your answer: ')
            if third_answer != third_true_answer:
                print("'" + third_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + third_true_answer + "'.")
                print("Let's try again, " + name + "!")
            else:
                print('Correct!')
                print('Congratulations, ' + name + '!')

if __name__ == '__main__':
    main()
