

import random
from brain_games.engine import is_prime


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def tasking():
    question = random.randint(2, 100)
    correct_answer = str(is_prime(question))
    return question, correct_answer
