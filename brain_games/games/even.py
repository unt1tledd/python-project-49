

import random


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    question % 2 == 0


def tasking():
    question = random.randint(1, 100)
    correct_answer = str(is_even(question))
    return question, correct_answer
