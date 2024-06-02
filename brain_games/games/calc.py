import random


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_question():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 20)
    operation = random.choice(operations)
    question = f"{num1} {operation} {num2}"
    correct_answer = str(eval(question))
    return question, correct_answer


def launch_game(name):
    print("What is the result of the expression?")

    correct_answers_count = 0
    rounds_to_win = 3

    while correct_answers_count < rounds_to_win:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers_count == rounds_to_win:
        print(f"Congratulations, {name}!")


def main():
    name = welcome_user()
    launch_game(name)


if __name__ == "__main__":
    main()
