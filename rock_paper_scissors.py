
# Rock-Paper-Scissors Game
import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
comp_score = 0

while True:
    user = input("Choose rock, paper, or scissors (or 'exit'): ").lower()
    if user == 'exit':
        break
    if user not in choices:
        print("Invalid choice.")
        continue
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or          (user == "paper" and comp == "rock") or          (user == "scissors" and comp == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        comp_score += 1

    print(f"Score - You: {user_score}, Computer: {comp_score}")
