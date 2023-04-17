import prompt


def engine(game, MAIN_QUESTION):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(MAIN_QUESTION)
    for i in range(3):
        question, true_answer = game()
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != true_answer:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{true_answer}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
    print('Congratulations, ' + name + '!')
