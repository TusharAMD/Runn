import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paper Plane Game")

# Load images
background_image = pygame.image.load("background.jpg")  # Replace with your image file
plane_image = pygame.image.load("planne.png")  # Replace with your image file
plane_rect = plane_image.get_rect()

# Set up the player
player_speed = 5
player_x = WIDTH // 2 - plane_rect.width // 2
player_y = HEIGHT - plane_rect.height - 20

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - plane_rect.width:
        player_x += player_speed

    # Update the display
    screen.fill(WHITE)
    screen.blit(background_image, (0, 0))
    screen.blit(plane_image, (player_x, player_y))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
