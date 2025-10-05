import pygame
from pathlib import Path

class TextObject():
    def __init__(self, displayText: str, fontUri: str, fontSize: int, color: tuple[int,int,int]):
        self.font = pygame.font.Font(Path(fontUri), fontSize)
        self.text = displayText
        self.color = color
        self.built = self.font.render(displayText, True, self.color)

    def getCompiled(self):
        return self.built