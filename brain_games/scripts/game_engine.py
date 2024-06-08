import prompt


def launch_game(game_module):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.GAME_DESCRIPTION)
    question, correct_answer = game_module.generate_question()
    print(f"Question: {question}")

    if hasattr(game_module, 'get_user_answer'):
        user_answer = game_module.get_user_answer()
    else:
        user_answer = prompt.string("Your answer: ")

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(
            f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'"
        )
        print(f"Let's try again, {name}!")
