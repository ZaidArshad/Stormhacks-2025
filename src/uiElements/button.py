import pygame
from uiElements.baseUIElement import baseUIElement
from uiElements.TextObject import TextObject

class Button(baseUIElement):
    def __init__(self, x, y,  buttonAssetUri:str, buttonHoverAssetUri:str = "", callback: any = None, TextObject: TextObject = None):
        super().__init__(x, y, buttonAssetUri = buttonAssetUri, textObj=TextObject)
        self.baseImage = pygame.image.load(buttonAssetUri).convert_alpha()

        self.hoveredImage = None
        if (buttonHoverAssetUri):
            self.hoveredImage = pygame.image.load(buttonHoverAssetUri).convert_alpha()

        self.collideRect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.callback = callback

    def check_hovered(self, pos):
        if (not self.hoveredImage):
            return

        if (self.collideRect.collidepoint(pos)):
            self.image = self.hoveredImage
        else:
            self.image = self.baseImage

    def is_clicked(self, pos):
        return self.collideRect.collidepoint(pos)
    
    def execCallback(self):
        return self.callback()