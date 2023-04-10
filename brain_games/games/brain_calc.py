import random
import prompt
#from brain_welcome.py import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
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
    
    second_exp_first_number = random.randint(0, 100)
    second_exp_second_number = random.randint(0, 100)
    second_exp_oper_number = random.randint(1, 3)
    if second_exp_oper_number == 1:
        second_exp_true_answer = second_exp_first_number + second_exp_second_number
        second_exp_char = '+'
    elif second_exp_oper_number == 2:
        second_exp_true_answer = second_exp_first_number - second_exp_second_number
        second_exp_char = '-'
    else:
        second_exp_true_answer = second_exp_first_number * second_exp_second_number
        second_exp_char = '*'

    third_exp_first_number = random.randint(0, 100)
    third_exp_second_number = random.randint(0, 100)
    third_exp_oper_number = random.randint(1, 3)
    if third_exp_oper_number == 1:
        third_exp_true_answer = third_exp_first_number + third_exp_second_number
        third_exp_char = '+'
    elif third_exp_oper_number == 2:
        third_exp_true_answer = third_exp_first_number - third_exp_second_number
        third_exp_char = '-'
    else:
        third_exp_true_answer = third_exp_first_number * third_exp_second_number
        third_exp_char = '*'
    
    print('Question: ' + str(first_exp_first_number) + ' ' + first_exp_char + ' ' + str(first_exp_second_number))
    first_answer = prompt.string('Your answer: ')
    if int(first_answer) != first_exp_true_answer:
        print("'" + first_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(first_exp_true_answer) + "'.")
        print("Let's try again, " + name + "!")
    else:
        print('Correct!')
        print('Question: ' + str(second_exp_first_number) + ' ' + second_exp_char + ' ' + str(second_exp_second_number))
        second_answer = prompt.string('Your answer: ')
        if int(second_answer) != second_exp_true_answer:
            print("'" + second_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(second_exp_true_answer) + "'.")
            print("Let's try again, " + name + "!")
        else:
            print('Correct!')
            print('Question: ' + str(third_exp_first_number) + ' ' + third_exp_char + ' ' + str(third_exp_second_number))
            third_answer = prompt.string('Your answer: ')
            if int(third_answer) != third_exp_true_answer:
                print("'" + third_answer + "'" + ' is wrong answer ;(. Correct answer was ' + "'" + str(third_exp_true_answer) + "'.")
                print("Let's try again, " + name + "!")
            else:
                print('Correct!')
                print('Congratulations, ' + name + '!')

if __name__ == '__main__':
    main()
