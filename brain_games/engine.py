

import random
import prompt
from brain_games.cli import welcome_user


def is_even(question):
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def creating_progress():
    progression = []
    num1 = random.randint(0, 10)
    num2 = random.randint(90, 100)
    st = random.randint(1, 10)
    for i in range(num1, num2, st):
        progression.append(i)
    return progression


def arithmetic_operations(operation, number1, number2):
    if operation == '+':
        correct_answer = number1 + number2
    elif operation == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    return result


def dividing(num):
    b = 0
    for i in range(2, 9):
        if (num % i) == 0:
            b += 1
    return b


def is_prime(num):
    b = dividing(num)
    if (num >= 9 and b > 0) or (num <= 9 and b > 1):
        return 'no'
    else:
        return 'yes'


def check_the_answer(question, correct_answer):
    print(f"Question: {question}")
    answer = prompt.string('Your answer: ')
    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}")
        return False


def logic_of_game(name_of_game):
    name = welcome_user()
    print(name_of_game.rule)
    a = 3
    while a > 0:
        question, correct_answer = name_of_game.tasking()
        if check_the_answrer(question, correct_answer):
            a -= 1
            if a == 0:
                print(f'Congratulations, {name}!')
            else:
                continue
        else:
            print(f"Let's try again, {name}!")
            break
