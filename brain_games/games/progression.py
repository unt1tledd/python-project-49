import random


RULE_OF_GAME = 'What number is missing in the progression?'


def create_progression():
    progression = []
    num1 = random.randint(0, 10)
    num2 = random.randint(90, 100)
    st = random.randint(1, 10)
    for i in range(num1, num2, st):
        progression.append(i)
    return progression


def generate_round():
    progression = create_progression()
    num_to_hide = random.randint(1, 9)
    correct_answer = str(progression[num_to_hide])
    progression[num_to_hide] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer
