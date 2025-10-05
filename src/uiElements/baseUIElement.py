import pygame
class baseUIElement:

    def __init__(self, x, y, buttonAssetUri = None, surface = None):
        if buttonAssetUri != None:
            self.image = pygame.image.load(buttonAssetUri).convert()
        elif surface != None:
            self.image = surface
        self.position = (x, y)

    def getSurface(self):
        return self.image
    
    def getPosition(self):
        return self.position