import random


MAIN_QUESTION = 'What is the result of the expression?'


def question_answer_generation():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    oper_number = random.randint(1, 3)
    if oper_number == 1:
        true_answer = str(first_number + second_number)
        exp_char = '+'
    elif oper_number == 2:
        true_answer = str(first_number - second_number)
        exp_char = '-'
    else:
        true_answer = str(first_number * second_number)
        exp_char = '*'
    question = f"{first_number} {exp_char} {second_number}"
    return question, true_answer
