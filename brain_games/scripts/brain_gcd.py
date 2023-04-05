import random
import prompt
from math import gcd
#from brain_welcome.py import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    first_q_first_number = random.randint(0, 100)
    first_q_second_number = random.randint(0, 100)
    first_q_gcd_number = gcd(first_q_first_number, first_q_second_number)

    second_q_first_number = random.randint(0, 100)
    second_q_second_number = random.randint(0, 100)
    second_q_gcd_number = gcd(second_q_first_number, second_q_second_number)

    third_q_first_number = random.randint(0, 100)
    third_q_second_number = random.randint(0, 100)
    third_q_gcd_number = gcd(third_q_first_number, third_q_second_number)
    
    print('Question: ' + str(first_q_first_number) + ' ' + str(first_q_second_number))
    first_answer = prompt.string('Your answer: ')
    if int(first_answer) != first_q_gcd_number:
        print("'" + first_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(first_q_gcd_number) + "'.")
        print("Let's try again, " + name + "!")
    else:
        print('Correct!')
        print('Question: ' + str(second_q_first_number) + ' ' + str(second_q_second_number))
        second_answer = prompt.string('Your answer: ')
        if int(second_answer) != second_q_gcd_number:
            print("'" + second_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(second_q_gcd_number) + "'.")
            print("Let's try again, " + name + "!")
        else:
            print('Correct!')
            print('Question: ' + str(third_q_first_number) + ' ' + str(third_q_second_number))
            third_answer = prompt.string('Your answer: ')
            if int(third_answer) != third_q_gcd_number:
                print("'" + third_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(third_q_gcd_number) + "'.")
                print("Let's try again, " + name + "!")
            else:
                print('Correct!')
                print('Congratulations, ' + name + '!')

if __name__ == '__main__':
    main()
