

import random


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    b = 0
    for i in range(2, num // 2 + 1):
        if (num % i) == 0:
            b += 1
    if b <= 0:
        return 'no'
    else:
        return 'yes'


def tasking():
    question = random.randint(2, 100)
    correct_answer = str(is_prime(question))
    return question, correct_answer
