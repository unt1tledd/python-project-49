import random


RULE_OF_GAME = 'What is the result of the expression?'


def count(operation, number1, number2):
    if operation == '+':
        correct_answer = number1 + number2
    elif operation == '-':
        correct_answer = number1 - number2
    elif operation == '*':
        correct_answer = number1 * number2
    return correct_answer


def play_round():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    question = f"{number1} {operation} {number2}"
    correct_answer = str(count(operation, number1, number2))
    return question, correct_answer
