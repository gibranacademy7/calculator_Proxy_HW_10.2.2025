from abstract_input_template import InputTemplate

class EmailInput(InputTemplate):
    def get_input(self):
        while True:
            user_input = input("Enter a valid email address: ")
            if self.validate_input(user_input):
                return user_input

    def validate_input(self, user_input):
        if "@" in user_input and user_input.index("@") > 0 and user_input.rindex("@") < len(user_input) - 1:
            return True
        else:
            print("Invalid email format. Please include a valid '@' character with text before and after.")
            return False
