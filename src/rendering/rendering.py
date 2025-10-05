import pygame
from uiElements.baseUIElement import baseUIElement
import math

OFFSET_X_SCALE = 10
OFFSET_Y_SCALE = 10
LAPTOP_VIEW_MARGIN_X = 100
LAPTOP_VIEW_MARGIN_Y = 100

class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.elements: list[baseUIElement] = []
        self.background = pygame.transform.scale( 
            pygame.image.load('assets/placeholder/main_bg.png').convert(),
            (self.screen.get_width()+200, self.screen.get_height()+100))

        self.laptop_view = pygame.Surface((self.screen.get_width()-LAPTOP_VIEW_MARGIN_X, 
                                          self.screen.get_height()-LAPTOP_VIEW_MARGIN_Y))
        self.laptop_view.fill("blue")

        self.fade_view = pygame.Surface(self.get_screen_size(), pygame.SRCALPHA)
        self.fade_view.fill("black")

        self.x_offset = 0
        self.y_offset = 0
        self.fade_opacity = 0
        self.delta_fade_opacity = 0

        self.is_laptop_view = False

    def get_screen_size(self):
        return (self.screen.get_width(), self.screen.get_height())

    def set_camera_offset(self, mouse_x, mouse_y):
        self.x_offset = (self.background.get_width()//2-mouse_x)/OFFSET_X_SCALE - 100
        self.y_offset = (self.background.get_height()//2-mouse_y)/OFFSET_Y_SCALE - 50

    def add_element(self, element):
        self.elements.append(element)

    def set_elements(self, elements):
        self.elements.clear()
        self.elements = elements

    def get_screen(self):
        return self.background
    
    def get_background(self):
        return self.background

    def draw(self):
        self.screen.fill("black")

        if self.is_laptop_view:
            self.screen.blit(self.laptop_view, (self.x_offset+LAPTOP_VIEW_MARGIN_X/2, self.y_offset+LAPTOP_VIEW_MARGIN_Y/2))
        else:
            for element in self.elements:
                pos = element.getPosition()
                self.background.blit(element.getSurface(), (pos[0], pos[1]))
            self.screen.blit(self.background, (self.x_offset, self.y_offset))

        if self.delta_fade_opacity != 0:
            self.fade()
            return
        

    def toggle_laptop_view(self):
        self.delta_fade_opacity = 10

    def fade(self):
        if (self.fade_opacity == 255):
            self.is_laptop_view = not self.is_laptop_view
            self.delta_fade_opacity = -10
        self.fade_opacity = max(0, min(self.fade_opacity+self.delta_fade_opacity, 255))
        self.fade_view.fill((0, 0, 0, self.fade_opacity))
        self.screen.blit(self.fade_view, (0, 0))
        if (self.fade_opacity == 0):
            self.delta_fade_opacity = 0
