import random
import prompt
from math import gcd

#from brain_welcome.py import welcome_user

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    general_counter = 0

    while general_counter < 3:

        number = random.randint(1, 100)
        print(number)
        true_answer = 'yes'
        if number == 1:
            true_answer = 'yes'
        else:
            for i in range(2, number):
                if (number % i) == 0:
                    true_answer = 'no'
                    break
        #print(true_answer)
        print('Question: ' + str(number))
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) != str(true_answer):
            print("'" + user_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(true_answer) + "'.")
            print("Let's try again, " + name + "!")
            break
        else:
            print('Correct!')
        general_counter += 1
        if general_counter == 3:
            print('Congratulations, ' + name + '!')



if __name__ == '__main__':
    main()
