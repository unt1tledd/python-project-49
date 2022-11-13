

import random


RULE_OF_GAME = 'What number is missing in the progression?'


def create_progress():
    progression = []
    num1 = random.randint(0, 10)
    num2 = random.randint(90, 100)
    st = random.randint(1, 10)
    for i in range(num1, num2, st):
        progression.append(i)
    return progression


def play_round():
    progression = create_progress()
    num = random.randint(1, 9)
    correct_answer = str(progression[num])
    progression[num] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer
