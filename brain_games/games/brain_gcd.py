import random
import prompt
from math import gcd
from brain_games.cli import welcome_user, name


def check(user_answer, true_answer):
    if str(user_answer) != str(true_answer):
        print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{str(true_answer)}'.")
        print(f"Let's try again, {name}!")
        return False
    else:
        print('Correct!')


def main():
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for i in range(0, 3):
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 100)
        true_answer = gcd(first_number, second_number)
        print('Question: ' + str(first_number) + ' ' + str(second_number))
        user_answer = prompt.string('Your answer: ')
        if check(user_answer, true_answer) is False:
            break
        if i == 2:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
