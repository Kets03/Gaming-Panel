import pygame
import random
from AllFunctions import *

def asteroid(playid):
    global playerid,highscore
    highscore=0
    playerid = playid
    # Initialize Pygame
    pygame.init()

    # Set the screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the title of the game window
    pygame.display.set_caption("Asteroid Game")

    # Set the clock to control the framerate
    clock = pygame.time.Clock()

    # Load the images
    player_image = pygame.image.load(".\\resources\\alienblaster.png")
    asteroid_image = pygame.image.load(".\\resources\\Asteroid.jpeg")

    # Set the player position
    player_x = screen_width / 2
    player_y = screen_height / 2

    # Set the player speed
    player_speed = 5

    # Set the asteroid positions and speeds
    asteroid_x = random.randint(0, screen_width)
    asteroid_y = random.randint(0, screen_height)
    asteroid_speed_x = random.randint(-5, 5)
    asteroid_speed_y = random.randint(-5, 5)

    # Set the score
    score = 0

    for row in fetchscores(playerid):
        highscore = row[1]

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the game
                pygame.quit()

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < screen_width - player_image.get_width():
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        elif keys[pygame.K_DOWN] and player_y < screen_height - player_image.get_height():
            player_y += player_speed

        # Move the asteroid
        asteroid_x += asteroid_speed_x
        asteroid_y += asteroid_speed_y

        # Check if the asteroid has hit the player
        if abs(player_x - asteroid_x) < player_image.get_width() and abs(
                player_y - asteroid_y) < player_image.get_height():
            # Game over
            print("Game over! Your score was", score)
            pygame.quit()

        # Check if the asteroid has gone off the screen
        if asteroid_x < 0 or asteroid_x > screen_width or asteroid_y < 0 or asteroid_y > screen_height:
            # Respawn the asteroid
            asteroid_x = random.randint(0, screen_width)
            asteroid_y = random.randint(0, screen_height)
            asteroid_speed_x = random.randint(-5, 5)
            asteroid_speed_y = random.randint(-5, 5)
            score += 1


        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the player and the asteroid
        screen.blit(player_image, (player_x, player_y))
        screen.blit(asteroid_image, (asteroid_x, asteroid_y))

        # Update the screen
        pygame.display.update()

        if(score>highscore):
            highscore=score
            updateasteroid(playerid,highscore)

        # Control the framerate
        clock.tick(60)