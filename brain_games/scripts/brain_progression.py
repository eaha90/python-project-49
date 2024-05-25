import random


def generate_progression(length, step):
    start = random.randint(1, 50)
    progression = [start + i * step for i in range(length)]
    return progression


def play_progression():
    print("brain-progression")
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers = 0
    while correct_answers < 3:
        length = random.randint(5, 10)
        step = random.randint(1, 10)
        progression = generate_progression(length, step)

        hidden_index = random.randint(0, length - 1)
        hidden_value = progression[hidden_index]
        progression[hidden_index] = ".."

        print(f"Question: {' '.join(str(x) for x in progression)}")
        answer = input("Your answer: ")

        try:
            answer = int(answer)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if answer == hidden_value:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{hidden_value}'.")
            print(f"Let's try again, {name}!")

    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_progression()
