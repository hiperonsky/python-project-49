import random


MAIN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_answer_generation():
    first_number = random.randint(0, 100)
    question = str(first_number)
    if first_number % 2 == 0:
        true_answer = 'yes'
    else:
        true_answer = 'no'
    return question, true_answer
