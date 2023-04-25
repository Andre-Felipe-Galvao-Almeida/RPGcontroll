from library import *

class Combat():
    def __init__(self):
        self.__round = 0
        self.grid = matriz()

    def RoundPass(self):
        self.__round += 1