from number_input import NumberInput
from email_input import EmailInput

def main():
    print("Number Input:")
    number_input = NumberInput()
    valid_number = number_input.get_input()
    print(f"You entered a valid number: {valid_number}")

    print("\nEmail Input:")
    email_input = EmailInput()
    valid_email = email_input.get_input()
    print(f"You entered a valid email: {valid_email}")

if __name__ == "__main__":
    main()
