from Guess_word import Guess
from Picking_word import RandWord
from Stopwatch import Timer
from Check_guess import Check
from Blank_word import Blank
from Past_results import Results

class Game:
    def __init__(self) -> None:
        self.count = 0
        pick_word = RandWord()
        self.answer = pick_word.word()


    def play(self):
       
        timer_go.start_timer()  # Start Timer
        while self.count < 8:
            guess_go.game_play()
            check_go.verify()
            board_go.display()
            if Check.verify() == True:
                print('Congrats!!! You have guessed right.')
                timer_go.stop_timer()   # Stop Timer
                timer_go.elapsed_time() # Display total Time
                results_go.save()
                break

        

results_go = Results()
check_go = Check()
guess_go = Guess()
board_go = Blank()
timer_go = Timer()
game_go = Game()
print("The answer is", game_go.answer)

#Game
#Guess
# x x x x x 
# x x x x x
# x x x x x
# x x x x x
# x x x x x