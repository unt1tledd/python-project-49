
import random
from brain_games.engine import arithmetic_operations


rule = 'What is the result of the expression?'


def tasking():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"
    correct_answer = str(arithmetic_operations(operation, number1, number2))
    return question, correct_answer
