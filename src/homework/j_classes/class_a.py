import random

class die:
    
    
    
    def roll(self):
        return random.randint(1,6)

    def get_rolled_value(self):

            return self.roll_value
        
    def __str__(self):

            print(f'The rolled value is: {self.roll_value}')
    