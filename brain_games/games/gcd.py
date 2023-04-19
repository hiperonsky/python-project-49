import random


MAIN_QUESTION = 'Find the greatest common divisor of given numbers.'


def gcd_find(first_number, second_number):
    while second_number:
        first_number, second_number = second_number, first_number \
            % second_number
    return first_number


def question_answer_generation():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    true_answer = str(gcd_find(first_number, second_number))
    question = str(first_number) + ' ' + str(second_number)
    return question, true_answer
