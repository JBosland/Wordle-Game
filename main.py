from Stopwatch import Timer
from Check_guess import Check
from Blank_word import Blank
from Past_results import Results
from termcolor import colored
class Game:

    """
    This class controls the whole game

    Paramters:
        self.count = 0 # S
        self.results_go = results_go # Object for Past_results
        self.check_go = check_go # Object for Check_guess
        self.timer_go = timer_go # Object for Stopwatch
        self.board_go = board_go # Object for Blankword
    """
    def __init__(self) -> None:
        self.count = 0
        results_go = Results()
        check_go = Check()
        board_go = Blank()
        timer_go = Timer()
        self.results_go = results_go
        self.check_go = check_go
        self.timer_go = timer_go
        self.board_go = board_go

    def play(self):
        # Starts timer
        self.timer_go.start_timer()  
        guess = input('Guess a 6 letter word:')
        while self.count < 8:
            
            # Call the verify funstion in Check_guess with guess as an input value
            self.check_go.verify(guess)
            print('')
            # Displays board
            self.board_go.display
            # Where user inputs guess
            guess = input('Guess a 6 letter word:')
            # Keeps track of guesses
            self.count += 1
            # if self.check_go.verify() == True:
            #     print('Congrats!!! You have guessed right.')
            #     self.timer_go.stop_timer()   # Stop Timer
            #     self.timer_go.elapsed_time() # Display total Time
            #     self.results_go.save()
            #     break
            # elif self.check_go.verify() != True and self.count == 8:
            #     print('Sorry, you have lost the game.')
game_go = Game()
game_go.play()
#Game
#Guess
# x x x x x 
# x x x x x
# x x x x x
# x x x x x
# x x x x x