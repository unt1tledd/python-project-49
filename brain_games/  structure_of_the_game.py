

import random
import prompt


def ev(question):
    if question % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


def num_in_list():
    numbers = []
    num1 = random.randint(0, 10)
    num2 = random.randint(90, 100)
    st = random.randint(1, 10)
    for i in range(num1, num2, st):
        numbers.append(i)
    return numbers


def arifm(operation, number1, number2):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    return result


def delimost(num):
    b = 0
    for i in range(2, 9):
        if (num % i) == 0:
            b += 1
    return b


def pr(num):
    b = delimost(num)
    if (num >= 9 and b > 0) or (num <= 9 and b > 1):
        return 'no'
    else:
        return 'yes'


def check(question, result):
    print(f"Question: {question}")
    answer = prompt.string('Your answer: ')
    if result == answer:
        print('Correct!')
        return True
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {result}")
        return False


def logic_of_game(name_of_game):
    name = welcome_user()
    print(name_of_game.rule)
    a = 3
    while a > 0:
        question, result = name_of_game.task()
        if check(question, result):
            a -= 1
            if a == 0:
                print(f'Congratulations, {name}!')
            else:
                continue
        else:
            print(f"Let's try again, {name}!")
            break
