from Guess_word import Guess
from termcolor import colored
from Picking_word import RandWord  

class Check(Guess, RandWord):
    def __init__(self) -> None:
            super().__init__()


    def verify(self):
            x = RandWord.word
            for i in range(min(len(self.guess),6)):
                # Checks if letter in position i in guess is the same as the letter in position i in c
                if self.guess[i] == x[i]:
                    # Prints letter in posiotion i in guess green
                    print(colored(self.guess[i], 'green'), end="")
                # Checks if letter in position i in guess is in c
                elif self.guess in x:
                    # Prints letter in posiotion i in guess green
                    print(colored(self.guess[i], 'yellow'), end="")

                else:
                    # Prints letter in position i in guess
                    print(self.guess[i], end="")

                if self.guess == x:

                    return True

app = Check()
app()