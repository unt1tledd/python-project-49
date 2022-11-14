import random


RULE_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    check = (question % 2 == 0)
    return check


def generate_round():
    question = random.randint(1, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
