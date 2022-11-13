

import random


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    question % 2 == 0


def tasking():
    question = random.randint(1, 100)
    check = is_even(question)
    if check == True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
