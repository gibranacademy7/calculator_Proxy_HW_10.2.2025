from abstract_input_template import InputTemplate

class NumberInput(InputTemplate):
    def get_input(self):
        while True:
            user_input = input("Enter a number between 1 and 100: ")
            if self.validate_input(user_input):
                return int(user_input)

    def validate_input(self, user_input):
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid integer.")
            return False
        number = int(user_input)
        if 1 <= number <= 100:
            return True
        else:
            print("Number must be between 1 and 100.")
            return False
