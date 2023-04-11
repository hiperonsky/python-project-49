import random
import prompt
from math import gcd
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    general_counter = 0
    while general_counter < 3:
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 100)
        true_answer = gcd(first_number, second_number)
        print('Question: ' + str(first_number) + ' ' + str(second_number))
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) != str(true_answer):
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
