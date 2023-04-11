import random
import prompt
from math import gcd
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('Find the greatest common divisor of given numbers.')
    general_counter = 0

    while general_counter < 3:
        first_q_first_number = random.randint(0, 100)
        first_q_second_number = random.randint(0, 100)
        first_q_gcd_number = gcd(first_q_first_number, first_q_second_number)
        print('Question: ' + str(first_q_first_number) + ' ' + str(first_q_second_number))
        first_answer = prompt.string('Your answer: ')
        if str(first_answer) != str(first_q_gcd_number):
            print("'" + first_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(first_q_gcd_number) + "'.")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
        general_counter += 1
        if general_counter == 3:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
