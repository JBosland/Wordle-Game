class Guess():
  
    def __init__(self) -> None:
        guess = input('What is the 6 letter word?')
        self.guess = guess

    def game_play(self):
        self.guess
        print(self.guess)


guess_go = Guess()
guess_go.game_play()