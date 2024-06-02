import random

GAME_DESCRIPTION = "Answer 'yes' if the number is even, otherwise answer 'no'."  # Описание игры


def even():
    print(GAME_DESCRIPTION)
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    rounds_count = 3
    for _ in range(rounds_count):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


def generate_question():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer
