import pygame.font
from pygame.sprite import Sprite

class Instructions(Sprite):

    def __init__(self, screen, settings):

        Sprite.__init__(self)
        self.screen = screen
        self.settings = settings

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont('Arial', 24)

        # Store the set of instructions
        self.instr_lines = ["Move your mouse to swipe the sword back and forth."]
        self.instr_lines.append("Or, click on the sword to grab it.")
        self.instr_lines.append("Keep your pop rate above 90%.")
        self.instr_lines.append("--- Please spare the kittens! ---")
        self.instr_lines.append("Letting a kitten live earns several balloons' worth of points;")
        self.instr_lines.append("Killing a kitten loses several balloons' worth of points.")

        # The instruction message only needs to be prepped once, not on every blit
        self.prep_msg()

    def prep_msg(self):
        y_position = self.settings.screen_height/2 + self.settings.button_height
        self.msg_images, self.msg_x, self.msg_y = [], [], []
        for index, line in enumerate(self.instr_lines):
            self.msg_images.append(self.font.render(line, True, self.text_color))
            self.msg_x.append(self.settings.screen_width/2-self.font.size(line)[0]/2)
            self.msg_y.append(y_position + index*self.font.size(line)[1])

    def blitme(self):
        for msg_x, msg_y, msg_image in zip(self.msg_x, self.msg_y, self.msg_images):
            self.screen.blit(msg_image, (msg_x, msg_y))
