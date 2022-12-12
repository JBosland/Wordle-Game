import random


class Randword():
        """
        This class opens a txt file, assigns all the words a number, 
        and uses a random number generator to pick a random word.

        Paramters:
        self.c = 0 # sets a initial value for c so the word can't be changed later
        words = {} # Creates a open dictionary for the words to go into
        """
        def __init__(self) -> None:
            # Dictionary for words
             words = {}
             self.words = words
             self.c = 0

        def word(self):
            # Opens the file with all of the words
            f = open('words.txt')

            # Counter to number the words
            j = 1
            for i in f:
                # Adds a word to the dictionary and assigns a number to it
                self.words[j] = i
                j += 1
            # Gets a random integer from 1 to 2500
            w = 2500
            n = random.randint(1,w)
            w -= 1
            if self.c == 0:
                self.c = self.words[n]
            else:
                self.c = self.c
            # Prints word with value of the number generated

            return str(self.c)


# For Testing Purposes
"""
app = Randword()
app.word()
"""
