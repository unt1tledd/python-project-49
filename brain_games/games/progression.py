

import random
from brain_games.cli import num_in_list


rule = 'What number is missing in the progression?'


def task():
    numbers = num_in_list()
    nom = random.randint(1, 9)
    result = str(numbers[nom])
    numbers[nom] = '..'
    question = " ".join(map(str, numbers[0:10]))
    return question, result
