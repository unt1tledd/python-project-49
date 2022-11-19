import prompt

MAX_ROUND = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE_OF_GAME)
    round_number = 0
    while round_number < MAX_ROUND:
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if correct_answer == answer:
            print('Correct!')
            round_number += 1
        else:
            print(f'{answer} is wrong answer ;(.')
            print(f'Correct answer was {correct_answer}')
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')
