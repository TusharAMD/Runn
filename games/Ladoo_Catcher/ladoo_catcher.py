import pygame
import sys
import random
import time  # Import the time module

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ladoo Catcher Game")

# Load images and resize them
catcher_img = pygame.image.load("net.png")
catcher_img = pygame.transform.scale(catcher_img, (50, 50))  # Resize the catcher image

ladoo_img = pygame.image.load("ladoo.png")
ladoo_img = pygame.transform.scale(ladoo_img, (30, 30))  # Resize the ladoo image

rock_img = pygame.image.load("asteroid.png")
rock_img = pygame.transform.scale(rock_img, (30, 30))  # Resize the rock image

# Set up the game clock
clock = pygame.time.Clock()

# Initial position of the catcher
catcher_x = WIDTH // 2
catcher_y = HEIGHT - 50

# Initial position of the items
ladoo_x = random.randint(0, WIDTH - 30)
ladoo_y = 0

rock_x = random.randint(0, WIDTH - 30)
rock_y = 0

# Set the speed of the items
item_speed = 5

# Initialize score
score = 0

# Font for displaying score and game state
font = pygame.font.Font(None, 36)

# Initial game state
game_state = "start"

# Timer for the start state
start_timer = 5  # Set the duration of the "Start" state in seconds

# Pause the game when it's over
pause_game = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Timer for the start state
    if game_state == "start" and start_timer > 0:
        start_timer -= 1
    else:
        game_state = "playing"

    # Pause the game when it's over
    if score < 0:
        game_state = "game over"
        pause_game = True
        print("Game Over!")

    # Move the catcher with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and catcher_x > 0:
        catcher_x -= 5
    if keys[pygame.K_RIGHT] and catcher_x < WIDTH - 50:
        catcher_x += 5

    # Move the items down the screen
    if not pause_game:
        ladoo_y += item_speed
        rock_y += item_speed

    # Check if the ladoo is caught
    if (
        catcher_x < ladoo_x < catcher_x + 50
        and catcher_y < ladoo_y < catcher_y + 50
    ):
        ladoo_x = random.randint(0, WIDTH - 30)
        ladoo_y = 0
        score += 10  # Increase score for catching ladoo
        print("Caught Ladoo! +10")

    # Check if the rock is caught
    if (
        catcher_x < rock_x < catcher_x + 50
        and catcher_y < rock_y < catcher_y + 50
    ):
        rock_x = random.randint(0, WIDTH - 30)
        rock_y = 0
        score -= 5  # Decrease score for catching rock
        print("Caught Rock! -5")

    # Check if the items reach the bottom
    if ladoo_y > HEIGHT:
        ladoo_x = random.randint(0, WIDTH - 30)
        ladoo_y = 0

    if rock_y > HEIGHT:
        rock_x = random.randint(0, WIDTH - 30)
        rock_y = 0

    # Draw the background
    screen.fill(WHITE)

    # Draw the catcher and items
    screen.blit(catcher_img, (catcher_x, catcher_y))
    screen.blit(ladoo_img, (ladoo_x, ladoo_y))
    screen.blit(rock_img, (rock_x, rock_y))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    # Draw game state
    state_text = font.render(game_state.capitalize(), True, RED)
    screen.blit(state_text, (WIDTH // 2 - 50, HEIGHT // 2))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(FPS)
