import pygame
import random
from AllFunctions import *


def dodge(playid):
    global playerid,highscore
    highscore=0
    playerid = playid
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    width = 500
    height = 500
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Block Dodge")

    # Set up the game clock
    clock = pygame.time.Clock()

    # Set up the player
    player_width = 50
    player_height = 50
    player_x = 225
    player_y = height - player_height
    player_speed = 3
    player = pygame.Rect(player_x, player_y, player_width, player_height)

    # Set up the obstacles
    obstacle_width = 50
    obstacle_height = 50
    obstacle_speed = 3
    obstacles = []

    # Set up the score
    score = 0
    font = pygame.font.SysFont(None, 30)

    for row in fetchscores(playerid):
        highscore = row[2]

    # Set up the game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < width - player_width:
            player.x += player_speed

        # Spawn new obstacles
        if len(obstacles) < 5:
            x = random.randint(0, width - obstacle_width)
            y = random.randint(-100, -50)
            obstacle = pygame.Rect(x, y, obstacle_width, obstacle_height)
            obstacles.append(obstacle)

        # Move the obstacles
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.y > height:
                obstacles.remove(obstacle)
                score += 1

            # Check for collisions
            if player.colliderect(obstacle):
                running = False

        # Update the screen
        window.fill((255, 255, 255))
        pygame.draw.rect(window, (0, 0, 0), player)
        for obstacle in obstacles:
            pygame.draw.rect(window, (255, 0, 0), obstacle)
        text = font.render("Score: " + str(score), True, (0, 0, 0))
        window.blit(text, (10, 10))
        pygame.display.update()

        if (score > highscore):
            highscore = score
            updatedodge(playerid, highscore)

        # Set the game clock
        clock.tick(60)

    # Quit Pygame
    pygame.quit()
#dodge(1132200001)