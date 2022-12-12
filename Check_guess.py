from termcolor import colored
from Picking_word import Randword 
class Check():
    """
    This class checks if the guess is equal to the random word

    Paramters:
    self.rand = RandWord() # Assigns Randword a self value to be called later in code
    """
    def __init__(self) -> None:
        self.rand = Randword()
    def verify(self, guess):
        self.guess = guess
        x = str(self.rand.word())

        if self.guess == x:

            return True
        
        for i in range (len(self.guess)):
            #print(x[i])
            #print(x[i])
            #print(self.guess[i])
            # Checks if letter in position i in guess is the same as the letter in position i in c
            if self.guess[i] == x[i]:
                # Prints letter in posiotion i in guess green
                print(colored(self.guess[i], 'green'), end="")
            # Checks if letter in position i in guess is in c
            elif self.guess[i] in x:
                # Prints letter in posiotion i in guess green
                print(colored(self.guess[i], 'yellow'), end="")

            else:
                # Prints letter in position i in guess
                print(self.guess[i], end="")
        
# For testing purposes
"""
guess_go = Check()
guess_go.verify()
"""
