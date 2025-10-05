import pygame

OFFSET_X_SCALE = 4
OFFSET_Y_SCALE = 4
LAPTOP_VIEW_MARGIN_X = 100
LAPTOP_VIEW_MARGIN_Y = 100

class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.elements = []
        self.background = pygame.Surface(self.get_screen_size())
        self.background.fill("red")

        self.laptop_view = pygame.Surface((self.screen.get_width()-LAPTOP_VIEW_MARGIN_X, 
                                          self.screen.get_height()-LAPTOP_VIEW_MARGIN_Y))
        self.laptop_view.fill("blue")

        self.x_offset = 0
        self.y_offset = 0
        self.fade_opacity = 0
        self.delta_opacity = 0

        self.is_laptop_view = False

    def get_screen_size(self):
        return (self.screen.get_width(), self.screen.get_height())

    def set_camera_offset(self, mouse_x, mouse_y):
        self.x_offset = (self.background.get_width()//2-mouse_x)/OFFSET_X_SCALE
        self.y_offset = (self.background.get_height()//2-mouse_y)/OFFSET_Y_SCALE

    def add_element(self, element):
        self.elements.append(element)

    def draw(self):
        self.screen.fill("black")

        if self.fade_opacity != 0:
            self.fade()
            return

        if self.is_laptop_view:
            self.screen.blit(self.laptop_view, (self.x_offset+LAPTOP_VIEW_MARGIN_X/2, self.y_offset+LAPTOP_VIEW_MARGIN_Y/2))
        else:
            for element in self.elements:
                self.background.blit(element, (0, 0))
            self.screen.blit(self.background, (self.x_offset, self.y_offset))

    def toggle_laptop_view(self):
        self.is_laptop_view = not self.is_laptop_view
        self.fade_opacity = 1

    def fade(self):
        self.screen.fill((0, 0, 0, self.fade_opacity))
