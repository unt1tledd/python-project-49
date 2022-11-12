

import random
from brain_games.engine import is_even


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def tasking():
    question = random.randint(1, 100)
    correct_answer = str(is_even(question))
    return question, correct_answer
