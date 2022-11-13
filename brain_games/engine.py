

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play(game):
    name = welcome_user()
    print(game.RULE_OF_GAME)
    a = 3
    while a > 0:
        question, correct_answer = game.play_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if correct_answer == answer:
            print('Correct!')
            a -= 1
            if a == 0:
                print(f'Congratulations, {name}!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            break
