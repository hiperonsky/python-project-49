import random
import prompt
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('What number is missing in the progression?')

    general_counter = 0

    while general_counter < 3:
        first_prog_first_number = random.randint(0, 100)
        first_prog_second_number = random.randint(0, 12)
        first_counter = 0
        first_list = []
        while first_counter < 10:
            first_list.append(first_prog_first_number)
            first_prog_first_number = first_prog_first_number + first_prog_second_number
            first_counter += 1
        first_prog_random_position = random.randint(0, 9)
        first_progr_true_answer = first_list[first_prog_random_position]
        first_list[first_prog_random_position] = '..'
        print('Question: ' + " ".join(map(str, first_list)))
        first_answer = prompt.string('Your answer: ')
        if str(first_answer) != str(first_progr_true_answer):
            print("'" + first_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(first_progr_true_answer) + "'.")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
        general_counter += 1
        if general_counter == 3:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
