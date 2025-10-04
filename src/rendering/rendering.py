import pygame

OFFSET_X_SCALE = 4
OFFSET_Y_SCALE = 4

class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.elements = []
        self.background = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.background.fill((255, 0, 0))
        self.x_offset = 0
        self.y_offset = 0

    def set_camera_offset(self, mouse_x, mouse_y):
        self.x_offset = (self.background.get_width()//2-mouse_x)/OFFSET_X_SCALE
        self.y_offset = (self.background.get_height()//2-mouse_y)/OFFSET_Y_SCALE

    def add_element(self, element):
        self.elements.append(element)

    def draw(self):
        self.screen.fill("black")

        for element in self.elements:
            self.background.blit(element, (0, 0))
        self.screen.blit(self.background, (self.x_offset, self.y_offset))
