# GameInit.py - Initializes PyGame and our game, and it contains the game loop.
# Created by Josh Kennedy on 17 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import os
import sys
import platform
import random
import time

import pygame

import Colors
import Vector2
import Circle
import CirclesGame

from Color import Color

# Initializes PyGame and its subsystems.
def initialize():
    # Set up environment variables for SDL (PyGame's subsystem).
    os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers the screen.

    if platform.system() == "Windows":
        os.environ["SDL_VIDEODRIVER"] = "directx" # If we're running Windows, then use the DirectX video driver.
    else:
        os.environ["SDL_VIDEO_GL_DRIVER"] = '1' # Otherwise, use OpenGL.

    # Initialize PyGame.
    pygame.init()

    # Initialize the window to 720p.
    screen = pygame.display.set_mode([1280, 720])
    pygame.display.set_caption("CirclesGame (Python Alpha)")

    # Clear the screen to white, and update it.
    screen.fill(Colors.White.getTuple())
    pygame.display.flip()

    # aaaand we're done!
    print(" done!")

# Kickstarts the game.
def start():
    print("Initializing and loading content...", end='')

    done = False # The condition in our game loop.
    fps = 60 # Our FPS, obviously.
    fpsClock = pygame.time.Clock() # The clock that's going to keep track of the current FPS.

    # Load the FPS font.
    font = pygame.font.Font("./Resources/Orbitron Medium.ttf", 20)

    # Initialize and seed the psuedo-random number generator.
    random.seed()

    # Create an instance of the Circle Game.
    circleGame = CirclesGame.CirclesGame()

    print(" done!\n")

    lastFrame = time.time()

    # The game loop.
    while not done:
        # Calculate the fps, and delta time.
        fpsClock.tick(fps)
        currentFrame = time.time()
        deltaTime = currentFrame - lastFrame
        lastFrame = currentFrame

        # Clear the screen.
        pygame.display.get_surface().fill(Colors.White.getTuple())

        # Update Game
        circleGame.update(deltaTime)

        # Draw Game
        circleGame.draw(deltaTime)

        # Draw the FPS
        drawFPSText(font, Vector2.Vector2(0, 0), "FPS: %6.3f" % fpsClock.get_fps(), Colors.Black, pygame.display.get_surface())

        # Update the screen.
        pygame.display.flip()
        pygame.display.update()

        # Handle input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            circleGame.handleInput(event)
        
    # Uninitialize PyGame.
    pygame.quit()

def drawFPSText(font, position, text, color, screen):
    textSurface = font.render(text, True, color.getTuple())
    screen.blit(textSurface, (position.x, position.y))
