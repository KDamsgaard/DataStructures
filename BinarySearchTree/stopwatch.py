"""
Kristian K. Damsgaard, 2019

A stopwatch timer.
"""

from datetime import datetime
import time

class Stopwatch():
    def __init__(self):
        self.__start = None
        self.__stop = None
    
    def start(self):
        self.__start = datetime.now()
    
    def stop(self):

        assert (self.__start is not None), "Stopwatch stopped before being started."
        self.__stop = datetime.now()

    def get_time_elapsed(self):
        return self.__stop - self.__start


#TESTING    ----------------------------------------------------------------------------------

timer = Stopwatch()

timer.start()

work = 0

for i in range (0, 10000000):
    work += 1


timer.stop()

print (timer.get_time_elapsed())