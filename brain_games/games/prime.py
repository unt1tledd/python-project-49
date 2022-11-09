

import random
from brain_games.cli import pr


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def task():
    question = random.randint(2, 100)
    result = str(pr(question))
    return question, result
