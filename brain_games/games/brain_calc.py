import random
import prompt
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('What is the result of the expression?')
    general_counter = 0

    while general_counter < 3:
        first_exp_first_number = random.randint(0, 100)
        first_exp_second_number = random.randint(0, 100)
        first_exp_oper_number = random.randint(1, 3)
        if first_exp_oper_number == 1:
            first_exp_true_answer = first_exp_first_number + first_exp_second_number
            first_exp_char = '+'
        elif first_exp_oper_number == 2:
            first_exp_true_answer = first_exp_first_number - first_exp_second_number
            first_exp_char = '-'
        else:
            first_exp_true_answer = first_exp_first_number * first_exp_second_number
            first_exp_char = '*'
        print('Question: ' + str(first_exp_first_number) + ' ' + first_exp_char + ' ' + str(first_exp_second_number))
        first_answer = prompt.string('Your answer: ')
        if str(first_answer) != str(first_exp_true_answer):
            print("'" + first_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(first_exp_true_answer) + "'.")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
            general_counter += 1
            if general_counter == 3:
                print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
