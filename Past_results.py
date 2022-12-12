from Stopwatch import Timer
from Check_guess import Check
class Results():
    """
    This class records the outcome and stats of the game into a txt file
    Paramters:
        super().__init__() # Contains the parameters from main
        self.check_go = check_go # Object for Check_guess
        self.timer_go = timer_go # Object for Stopwatch
    """
    def __init__(self) -> None:
        super().__init__()
        guess_go = Check()
        timer_go = Timer()
        self.check_go = guess_go
        self.timer_go = timer_go

    def save(self):


        with open('results.txt', 'w') as f:
            
            f.write(self.check_go.verify, self.count, self.timer_go.elapsed_time)
            


