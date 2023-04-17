import random


MAIN_QUESTION = 'Find the greatest common divisor of given numbers.'


def gcd_find(first_number, second_number):
    n = min(first_number, second_number)
    gcd_result = 0
    for i in range(1, n + 1):
        if first_number % i == 0 and second_number % i == 0:
            gcd_result = i
    return str(gcd_result)


def game():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    true_answer = gcd_find(first_number, second_number)
    question = str(first_number) + ' ' + str(second_number)
    return question, true_answer
