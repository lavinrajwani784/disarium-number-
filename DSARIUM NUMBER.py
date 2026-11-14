# Disarium Number Checker
# A number is Disarium if sum of its digits powered by their positions equals the number

def is_disarium(num):
    """
    Check if a number is a Disarium number.
    """
    # Convert number to string for digit extraction
    num_str = str(num)
    total = 0

    # Enumerate digits starting from position 1
    for i, digit in enumerate(num_str, start=1):
        total += int(digit) ** i

    return total == num


def main():
    try:
        # Input from user
        user_input = input("Enter a positive integer: ").strip()

        # Validate input
        if not user_input.isdigit():
            print("Invalid input. Please enter a positive integer.")
            return

        num = int(user_input)

        # Check and display result
        if is_disarium(num):
            print(f"{num} is a Disarium number ✅")
        else:
            print(f"{num} is NOT a Disarium number ❌")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
