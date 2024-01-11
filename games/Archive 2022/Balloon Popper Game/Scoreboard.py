import pygame, pygame.font
from pygame.sprite import Sprite


class Scoreboard(Sprite):

    def __init__(self, screen, settings):

        Sprite.__init__(self)
        self.screen = screen
        self.settings = settings

        self.initialize_stats()
        
        # Set dimensions and properties of scoreboard
        self.sb_height, self.sb_width = settings.scoreboard_height, self.screen.get_width()
        self.rect = pygame.Rect(0,0, self.sb_width, self.sb_height)
        self.bg_color=(100,100,100)
        self.text_color = (225,225,225)
        self.font = pygame.font.SysFont('Arial', 18)

        # Set positions of individual scoring elements on the scoreboard
        self.x_popped_position, self.y_popped_position = 20.0, 10.0
        self.x_ratio_position, self.y_ratio_position = 150, 10.0
        self.x_points_position, self.y_points_position = 350, 10.0
        self.x_score_position, self.y_score_position = self.screen.get_width() - 200, 10.0

    def initialize_stats(self):
        # Game attributes to track for scoring
        self.balloons_popped = 0
        self.balloons_missed = 0
        self.score = 0
        self.popped_ratio = 1.0
        self.batches_finished = 0
        self.kittens_spared = 0
        self.kittens_killed = 0

    def prep_scores(self):
        self.popped_string = "Popped: " + str(self.balloons_popped)
        self.popped_image = self.font.render(self.popped_string, True, self.text_color)

        self.score_string = "Score: " + format(self.score, ',d')
        self.score_image = self.font.render(self.score_string, True, self.text_color)

        self.set_ratio_string()
        self.popped_ratio_image = self.font.render(self.popped_ratio_string, True, self.ratio_text_color)

        self.points_string = "Points per Balloon: " + str(self.settings.points_per_balloon)
        self.points_image = self.font.render(self.points_string, True, self.text_color)

    def set_ratio_string(self):
        if self.popped_ratio == 1.0:
            self.popped_ratio_string = "Pop Rate: 100%"
        else:
            self.popped_ratio_string = "Pop Rate: " + "{0:.3}%".format(self.popped_ratio*100.0)
        if self.popped_ratio < 0.95:
            self.ratio_text_color = (255, 51, 51)
        else:
            self.ratio_text_color = self.text_color

    def blitme(self):
        # Turn individual scoring elements into images that can be drawn
        self.prep_scores()
        # Draw blank scoreboard
        self.screen.fill(self.bg_color, self.rect)
        # Draw individual scoring elements
        self.screen.blit(self.popped_image, (self.x_popped_position, self.y_popped_position))
        self.screen.blit(self.points_image, (self.x_points_position, self.y_points_position))
        self.screen.blit(self.score_image, (self.x_score_position, self.y_score_position))
        self.screen.blit(self.popped_ratio_image, (self.x_ratio_position, self.y_ratio_position))
