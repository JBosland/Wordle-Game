import random


class RandWord():

        def __init__(self) -> None:
            # Dictionary for words
             words = {}
             self.words = words

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
            c = self.words[n]
            # Prints word with value of the number generated
            # print(c)
            return c


# For Testing Purposes
#app = RandWord()
#app.word()

