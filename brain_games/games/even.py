

import random


RULE_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_round():
    question = random.randint(1, 100)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
