import random


main_question = 'What number is missing in the progression?'


def progression_find(first_number, second_number):
    counter = 0
    progression = []
    while counter < 10:
        progression.append(first_number)
        first_number = first_number + second_number
        counter += 1
    return progression


def progression_question(first_number, second_number, prog_random_position):
    progression = progression_find(first_number, second_number)
    progression[prog_random_position] = '..'
    return " ".join(map(str, progression))


def game():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 12)
    prog_random_position = random.randint(0, 9)
    true_answer = str(progression_find(
        first_number,
        second_number)[prog_random_position])
    question = str(progression_question(
        first_number,
        second_number,
        prog_random_position))
    return question, true_answer
