import random
from prompt_toolkit import prompt

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_user_answer():
    while True:
        answer = input("Your answer: ")
        try:
            answer = int(answer)
            if answer <= 0:
                print("Please enter a positive integer.")
            else:
                return answer
        except ValueError:
            print("Please enter a valid integer.")

def check_answer(answer, num1, num2):
    if answer == gcd(num1, num2):
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcd(num1, num2)}'.")
        return False

def play_round(name):
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    print(f"Question: {number1} {number2}")
    answer = get_user_answer()
    if answer is None:
        return False
    return check_answer(answer, number1, number2)

def main():
    name = prompt("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
    correct_answers = 0
    while correct_answers < 3:
        if play_round(name):
            correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
