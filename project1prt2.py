import random

# Define the choices and their corresponding values
# Using a dictionary for choices makes the code cleaner
choices = {
    "s": {"value": 1, "name": "Snake"},
    "w": {"value": -1, "name": "Water"},
    "g": {"value": 0, "name": "Gun"}
}

# Get computer's choice
computer_choice_value = random.choice([c["value"] for c in choices.values()])

# Get user's choice
while True: # Loop until a valid input is received
    user_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
    if user_input in choices:
        user_choice_value = choices[user_input]["value"]
        break # Exit loop if input is valid
    else:
        print("Invalid input. Please enter 's', 'w', or 'g'.")

# Determine names for display
user_choice_name = next(c["name"] for c in choices.values() if c["value"] == user_choice_value)
computer_choice_name = next(c["name"] for c in choices.values() if c["value"] == computer_choice_value)

#DISPLAT_CHOICES

print(f"\nYou chose: {user_choice_name}")
print(f"Computer chose: {computer_choice_name}")

# ---
## Determine the Winner

#The core logic of "Snake, Water, Gun" is about who beats whom. You can simplify your `if/elif` statements by thinking about the winning conditions:

# Snake (1) beats Water (-1)  
# Water (-1) beats Gun (0)
# Gun (0) beats Snake (1)

# Let's represent these winning conditions in a structured way.

if computer_choice_value == user_choice_value:
    print("It's a DRAW!")
else:
    # Define the winning conditions: (value_that_wins, value_that_loses)
    winning_conditions = [
        (1, -1),  # Snake (1) beats Water (-1)
        (-1, 0),  # Water (-1) beats Gun (0)
        (0, 1)    # Gun (0) beats Snake (1)
    ]

    # Check if the user's choice and the computer's choice match any winning condition
    if (user_choice_value, computer_choice_value) in winning_conditions:
        print("You WIN!")
    else:
        print("You LOSE!")