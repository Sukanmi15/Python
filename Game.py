import random

choices = ["rock", "paper", "scissors"]

print("🎮 ROCK, PAPER, SCISSORS 🎮")

while True:
    player = input("Choose rock, paper, or scissors (or type 'quit'): ").lower()

    if player == "quit":
        print("Thanks for playing! 👋")
        break

    if player not in choices:
        print("❌ Invalid choice. Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("🤝 It's a tie!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win!")

    else:
        print("😔 Computer wins!")

    print("----------------------")