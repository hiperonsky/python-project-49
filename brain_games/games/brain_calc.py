import random
import prompt
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('What is the result of the expression?')
    for i in range(0, 3):
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
        print(f"Question: {str(first_number)} {exp_char} {str(second_number)}")
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) != str(true_answer):
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{str(true_answer)}'.")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
        if i == 2:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
