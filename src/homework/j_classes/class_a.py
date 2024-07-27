import random

class die:
    
    
    def __init__(self):
        # Initialize roll_value with a default value
        self.roll_value = None

    def roll(self):
        # Generate a random value between 1 and 6 and store it in roll_value
            self.roll_value = random.randint(1, 6)


    def get_rolled_value(self):

            return self.roll_value
        
    def __str__(self):

            print(f'The rolled value is: {self.roll_value}')
    