import prompt


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')


def welcome_user():
    print('Hello, ' + name + '!')


def check(user_answer, true_answer):
    if str(user_answer) != str(true_answer):
        print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{str(true_answer)}'.")
        print(f"Let's try again, {name}!")
        return False
    else:
        print('Correct!')
