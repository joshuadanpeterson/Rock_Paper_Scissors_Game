import random
from modules.game_description import description

print(description)

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

while True:
  user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ")
  if user_choice == 'exit':
    print(f"Final score: You {user_score}, Computer {computer_score}")
    break
  if user_choice not in choices:
    print("Invalid choice. Try again.")
    continue

  computer_choice = random.choice(choices)
  print(f"Computer chose {computer_choice}")

  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!\n")
    user_score += 1
  else:
    print("Computer wins!\n")
    computer_score += 1

  print(f"Current score: You {user_score}, Computer {computer_score}")

  play_again = input("Do you want to play again? (yes/no): ")
  if play_again.lower() != 'yes' and play_again.lower() != 'y':
    print(f"Final score: You {user_score}, Computer {computer_score}")
    break
