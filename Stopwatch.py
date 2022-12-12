import time
#from Guess_word import Guess
class Timer():
    """
        This starts a timer to track howlong it takes for the user to finish
        playing the game
        Paramters:
        self.start_time = 0 # Sets initial start time to 0
        self.stop_time = 0 # Sets initial end time to 0
        """
    def __init__(self) -> None:
        self.start_time = 0
        self.stop_time = 0

    def start_timer(self):
        # Records time at moment
        self.start_time = time.time()

    def stop_timer(self):
        # Records time at moment
        self.stop_time = time.time()

    def elapsed_time(self):
        # Subtracts time to get elapsed time
        self.total_time = int(self.stop_time - self.start_time)
        print(self.total_time)


# For testing purposes
'''
timer_go = timer() 
timer_go.start_timer()
time.sleep(5)
timer_go.stop_timer()
timer_go.elapsed_time()
'''





