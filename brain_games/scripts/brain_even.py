from brain_games.games import even # type: ignore
from brain_games.scripts.game_engine import launch_game # type: ignore


def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def main():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    rounds_to_win = 3
    correct_answers_count = 0

    while correct_answers_count < rounds_to_win:
        question, correct_answer = even.generate_question()
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

if __name__ == "__main__":
    main()
