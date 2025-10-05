import pygame
from uiElements.baseUIElement import baseUIElement

class Button(baseUIElement):
    def __init__(self, x, y,  buttonAssetUri:str):
        super().__init__(x, y, buttonAssetUri = buttonAssetUri) 
        self.collideRect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def is_clicked(self, pos):
        # Check if a mouse position (x, y) is within the button's rectangle
        return self.collideRect.collidepoint(pos)