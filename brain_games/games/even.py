

import random
from brain_games.cli import ev


rule = 'Answer "yes" if the number is even, otherwise answer "no".'


def task():
    question = random.randint(1, 100)
    result = str(ev(question))
    return question, result
