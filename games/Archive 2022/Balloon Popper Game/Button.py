import pygame.font
from pygame.sprite import Sprite

class Button(Sprite):

    def __init__(self, screen, x_pos, y_pos, settings, msg):

        Sprite.__init__(self)
        self.screen = screen
        self.settings = settings

        # Set dimensions and properties of button
        self.width, self.height = settings.button_width, settings.button_height
        self.x_position, self.y_position = x_pos, y_pos
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
        self.font = pygame.font.SysFont(settings.button_font, settings.button_font_size)
        self.msg = msg        

        # Button message only needs to be prepped once, not on every blit
        self.prep_msg()

    def prep_msg(self):
        # Turn msg into image that can be rendered
        self.msg_image = self.font.render(self.msg, True, self.settings.button_text_color)
        # Determine offset to center text on button
        self.msg_x = self.x_position + (self.width - self.msg_image.get_width()) / 2
        self.msg_y = self.y_position + (self.height - self.msg_image.get_height()) / 2

    def blitme(self):
        # Draw blank button, and draw message
        self.screen.fill(self.settings.button_bg, self.rect)
        self.screen.blit(self.msg_image, (self.msg_x, self.msg_y))
