import random
from clock import Clock
class RandWord(Clock):
    #if Clock.get_time() == '00:00':
        def __init__(self) -> None:
             super().__init__()
             
        def word():
            # Opens the file with all of the words
            f = open('words.txt')
            # Dictionary for words
            k = {}
            # Counter to number the wors
            j = 1
            for i in f:
                # Adds a word to the dictionary and assigns a number to it
                k[j] = i
                j += 1
            # Gets a random integer from 1 to 500
            w = 2500
            n = random.randint(1,w)
            w -= 1
            # Prints word with value of the number generated
            return print(k[n])

