

import random


rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    b = 0
    for i in range(2, 9):
        if (num % i) == 0:
            b += 1
    return b


def tasking():
    num = random.randint(2, 100)
    b = str(is_prime(num))
    if (num >= 9 and b > 0) or (num <= 9 and b > 1):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return num, correct_answer
