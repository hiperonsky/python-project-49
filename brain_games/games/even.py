import random


main_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    first_number = random.randint(0, 100)
    question = str(first_number)
    if first_number % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return question, true_answer
