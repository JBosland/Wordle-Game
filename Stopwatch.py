import time
#from Guess_word import Guess
class Timer():
    # Sets time equal to 0 seconds
    
    def __init__(self) -> None:
        self.start_time = 0
        self.stop_time = 0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.stop_time = time.time()

    def elapsed_time(self):
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





