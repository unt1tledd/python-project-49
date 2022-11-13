
import random


RULE_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divs = 0
    for i in range(2, 9):
        if (num % i) == 0:
            divs += 1
    return divs


def play_round():
    num = random.randint(2, 100)
    divs = is_prime(num)
    if (num >= 9 and divs > 0) or (num <= 9 and divs > 1):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return str(num), correct_answer
