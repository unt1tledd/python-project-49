
import random
from brain_games.cli import arifm


rule = 'What is the result of the expression?'


def task():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    lists = ['+', '-', '*']
    operation = random.choice(lists)
    question = f"{number1} {operation} {number2}"
    result = str(arifm(operation, number1, number2))
    return question, result
