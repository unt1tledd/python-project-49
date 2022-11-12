

import random
from brain_games.engine import creating_progress


rule = 'What number is missing in the progression?'


def task():
    progression = creating_progress()
    num = random.randint(1, 9)
    correct_answer = str(progression[num])
    progression[num] = '..'
    question = " ".join(map(str, progression[0:10]))
    return question, correct_answer
