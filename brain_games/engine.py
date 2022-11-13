

import prompt
from brain_games.cli import welcome_user


def logic_of_game(name_of_game):
    name = welcome_user()
    print(name_of_game.rule)
    a = 3
    while a > 0:
        question, correct_ans = name_of_game.tasking()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if correct_ans == result:
            print('Correct!')
            a -= 1
            if a == 0:
                print(f'Congratulations, {name}!')
            else:
                continue
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_ans}")
            print(f"Let's try again, {name}!")
            break
