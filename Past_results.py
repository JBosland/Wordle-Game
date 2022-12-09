from main import Game
from Guess_word import Guess
from Stopwatch import Timer

class Results(Game):
        
    def __init__(self) -> None:
        super().__init__()
        

    def save(self):


        with open('results.txt', 'w') as f:
            
            f.write(guess_go.game_play, self.count, timer_go.elapsed_time)
            


game_go = Game()
guess_go = Guess()
timer_go = Timer()