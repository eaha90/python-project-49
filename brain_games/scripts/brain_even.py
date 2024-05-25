import random

print("Welcome to the Brain Games!")
name = input("May I have your name? ")
print(f"Hello, {name}!")
print('Answer "yes" if the number is even, otherwise answer "no".')


def play_even():
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").lower()

        if answer == "yes" and number % 2 == 0:
            print("Correct!")
            correct_answers += 1
        elif answer == "no" and number % 2 != 0:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(.")
            if number % 2 == 0:
                print(f"Correct answer was 'yes'.")
            else:
                print(f"Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_even()
