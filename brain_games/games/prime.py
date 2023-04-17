import random


MAIN_QUESTION = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def game():
    number = random.randint(1, 100)
    if is_prime(number):
        true_answer = 'yes'
    else:
        true_answer = 'no'
    question = str(number)
    return question, true_answer
