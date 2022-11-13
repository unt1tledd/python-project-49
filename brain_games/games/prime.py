

import random


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    b = 0
    for i in range(2, 9):
        if (num % i) == 0:
            b += 1
    if (num >= 9 and b > 0) or (num <= 9 and b > 1):
        return 'no'
    else:
        return 'yes'


def tasking():
    question = random.randint(2, 100)
    correct_answer = str(is_prime(question))
    return question, correct_answer
