

import random
import math


rule = 'Find the greatest common divisor of given numbers.'


def task():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    result = str(math.gcd(number1, number2))
    question = f"{number1} {number2}"
    return question, result
