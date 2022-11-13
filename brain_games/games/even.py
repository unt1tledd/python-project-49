

import random


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def tasking():
    question = random.randint(1, 100)
    correct_answer = str(is_even(question))
    return question, correct_answer
