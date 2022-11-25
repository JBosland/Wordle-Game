from Picking_word import RandWord


class Guess(RandWord):
    def __init__(self) -> None:
        super().__init__()
        guess = input('What is the 6 letter word?')
        self.guess = guess

    def game_play(self):
        print(RandWord.word())
        print(self.guess)
        if RandWord.word() == self.guess:
            return print('You have guessed the right word!!!')


Guess.game_play()