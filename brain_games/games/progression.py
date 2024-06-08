import random
import prompt

GAME_DESCRIPTION = 'Brain Progression'


def generate_question():

    start = random.randint(1, 10)
    step = random.randint(1, 10)
    progression_length = random.randint(5, 11)
    progression = [start + i * step for i in range(progression_length)]
    hidden_index = random.randint(0, progression_length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = f"Question: {' '.join(str(item) for item in progression)}"
    return question, correct_answer


def get_user_answer():

    return prompt.string("Your answer: ")


def launch_game(game_module):

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.GAME_DESCRIPTION)
    correct_answers_count = 0
    rounds_to_win = 3

    while correct_answers_count < rounds_to_win:
        question, correct_answer = game_module.generate_question()

        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'"
            )
            print(f"Let's try again, {name}!")
            break

    if correct_answers_count == rounds_to_win:
        print(f"Congratulations, {name}!")

if __name__ == "__main__":
    launch_game(globals())
