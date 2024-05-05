import random

print("Welcome to the Brain Games!")
name = input("May I have your name? ")
print(f"Hello, {name}!")
print('Answer "yes" if the number is even, otherwise answer "no".')

correct_answers = 0

while correct_answers < 3:
    number = random.randint(1, 100)
    print(f"Question: {number}")
    answer = input("Your answer: ")

    if (number % 2 == 0 and answer == "yes") or (number % 2 != 0 and answer == "no"):
        print("Correct!")
        correct_answers += 1
    else:
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f"'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.")
        break

if correct_answers == 3:
    print(f"Congratulations, {name}!")
