import random
import math

def gcd(a, b):
  """
  Функция для вычисления НОД двух чисел.
  """
  while b:
    a, b = b, a % b
  return a

def play_gcd():
  """
  Функция для игры "НОД".
  """
  print("brain-gcd")
  print("Welcome to the Brain Games!")
  name = input("May I have your name? ")
  print(f"Hello, {name}!")
  print("Find the greatest common divisor of given numbers.")

  correct_answers = 0
  while correct_answers < 3:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    print(f"Question: {num1} {num2}")
    answer = input("Your answer: ")

    try:
      answer = int(answer)
    except ValueError:
      print("Please enter a valid integer.")
      continue

    if answer == gcd(num1, num2):
      print("Correct!")
      correct_answers += 1
    else:
      print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcd(num1, num2)}'.")
      print(f"Let's try again, {name}!")

  if correct_answers == 3:
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
  play_gcd()