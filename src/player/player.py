from singletons.singletons import game, GameState
import pygame
from pathlib import Path

class Player:
    def __init__(self):
        self.sanity = 100
        self.hallucination = [False] * 6

    def lower_sanity(self, delta):
        self.sanity -= delta

        if self.sanity <= 90 and not self.hallucination[0]:
            self.hallucination[0] = True
            # change clock
            pass
        if self.sanity <= 85 and not self.hallucination[1]:
            self.hallucination[1] = True
            # book sound
        if self.sanity <= 75 and not self.hallucination[2]:
            self.hallucination[2] = True
            # strange words on notes
        if self.sanity <= 60 and not self.hallucination[3]:
            self.hallucination[3] = True
            # weird shadow
        if self.sanity <= 50 and not self.hallucination[4]:
            self.hallucination[4] = True
            # red bull logo bloody
        if self.sanity <= 35 and not self.hallucination[5]:
            self.hallucination[5] = True
            # laptop flashes red
        if self.sanity <= 0:
            pass
            # game.state = GameState.ENDINGSCREEN

    
    