import random
import prompt
from brain_games.cli import welcome_user, name


def prime_number(number):
    if number <= 1:
        return 'no'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(0, 3):
        number = random.randint(1, 100)
        true_answer = prime_number(number)
        print('Question: ' + str(number))
        user_answer = prompt.string('Your answer: ')
        if check(user_answer, true_answer) is False:
            break

        if i == 2:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
