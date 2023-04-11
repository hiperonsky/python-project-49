import random
import prompt
from brain_games.cli import welcome_user, name


def main():
    welcome_user()
    print('What number is missing in the progression?')
    for i in range(0, 3):
        first_number = random.randint(0, 100)
        second_number = random.randint(0, 12)
        counter = 0
        list = []
        while counter < 10:
            list.append(first_number)
            first_number = first_number + second_number
            counter += 1
        prog_random_position = random.randint(0, 9)
        true_answer = list[prog_random_position]
        list[prog_random_position] = '..'
        print('Question: ' + " ".join(map(str, list)))
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
