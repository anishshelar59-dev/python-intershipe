# Match-Case Example

# Take a choice from the user
choice = int(input("Enter your choice (1-4): "))

# Match the user's choice
match choice:

    # If choice is 1
    case 1:
        print("You selected Addition")

    # If choice is 2
    case 2:
        print("You selected Subtraction")

    # If choice is 3
    case 3:
        print("You selected Multiplication")

    # If choice is 4
    case 4:
        print("You selected Division")

    # Default case
    case _:
        print("Invalid choice")
