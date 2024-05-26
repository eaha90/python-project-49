import random


def get_user_name():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2


def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def play_game(name):
    print("Find the greatest common divisor of given numbers.")
    rounds = 3
    for _ in range(rounds):
        num1, num2 = generate_numbers()
        print(f"Question: {num1} {num2}")
        answer = int(input("Your answer: "))
        correct_answer = find_gcd(num1, num2)
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    name = get_user_name()
    play_game(name)

    if __name__ == "__main__":
        main()
