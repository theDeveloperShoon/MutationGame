# Externals
import sys
import os

import pygame

# Internals
from framework.Game import Game
from framework.SaveManager import jsonify_game_data, save_on_file, load_file


# Initializes Pygame
pygame.init()

clock = pygame.time.Clock()

game = Game()

# Display Setup
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 840
RESOLUTION = SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Mutator - The Mutation Experiment")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill("purple")
    pygame.display.flip()

    clock.tick(60) # Limits to 60 FPS

