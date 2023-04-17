import random
from math import gcd


main_question = 'Find the greatest common divisor of given numbers.'


def game():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    true_answer = gcd(first_number, second_number)
    question = str(first_number) + ' ' + str(second_number)
    return question, true_answer
