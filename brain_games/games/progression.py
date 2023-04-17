import random


MAIN_QUESTION = 'What number is missing in the progression?'


def progression_find(initial_term, members_difference):
    counter = 0
    progression = []
    while counter < 10:
        progression.append(initial_term)
        initial_term = initial_term + members_difference
        counter += 1
    return progression


def progression_question(initial_term,
                         members_difference,
                         prog_random_position):
    progression = progression_find(initial_term, members_difference)
    progression[prog_random_position] = '..'
    return " ".join(map(str, progression))


def question_answer_generation():
    initial_term = random.randint(0, 100)
    members_difference = random.randint(0, 12)
    prog_random_position = random.randint(0, 9)
    true_answer = str(progression_find(
        initial_term,
        members_difference)[prog_random_position])
    question = str(progression_question(
        initial_term,
        members_difference,
        prog_random_position))
    return question, true_answer
