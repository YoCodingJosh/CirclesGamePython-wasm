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

import AssetCache

import Colors
import Vector2
import Circle
import CirclesGame

from Color import Color

# Our global loop condition, so we can exit the game from the menu.
gameDone = False

# Initializes PyGame and its subsystems.
def initialize():
    print("Starting up..." , end='')

    # Set up environment variables for SDL (PyGame's subsystem).
    os.environ['SDL_VIDEO_CENTERED'] = '1' # Centers the screen.

    if platform.system() == "Windows":
        os.environ["SDL_VIDEODRIVER"] = "directx" # If we're running Windows, then use the DirectX video driver.
    else:
        os.environ["SDL_VIDEO_GL_DRIVER"] = '1' # Otherwise, use OpenGL.

    # Initialize PyGame TTF.
    pygame.font.init()

    # Initialize PyGame Mixer.
    pygame.mixer.pre_init(44100, -16, 1, 512)

    # Initialize PyGame.
    pygame.init()

    # Initialize the window to 720p.
    screen = pygame.display.set_mode([1280, 720], pygame.DOUBLEBUF | pygame.HWSURFACE)
    pygame.display.set_caption("CirclesGame (Python Alpha)", "Circle Game")

    # Set icon.
    pygame.display.set_icon(pygame.image.load("./Resources/Icon_Full.png"))

    # Clear the screen to white, and update it.
    screen.fill(Colors.White.getTuple())
    pygame.display.flip()

    # aaaand we're done!
    print(" done!")

# Kickstarts the game.
def start():
    global gameDone

    print("Initializing and loading content...", end='')

    fps = 60 # Our FPS, obviously.
    fpsClock = pygame.time.Clock() # The clock that's going to keep track of the current FPS.

    # Load and cache the assets.
    AssetCache.startCache("./Resources/")

    # Initialize and seed the pseudo-random number generator.
    random.seed()

    # Create an instance of the Circle Game.
    circleGame = CirclesGame.CirclesGame()

    print(" done!\n")

    lastFrame = time.time()

    # Set the initial value to gameDone
    gameDone = False

    gameTitle = "CirclesGame (Python Alpha)"

    # The game loop.
    while not gameDone:
        # Calculate the fps, and delta time.
        fpsClock.tick_busy_loop(fps)
        currentFrame = time.time()
        deltaTime = currentFrame - lastFrame
        lastFrame = currentFrame

        # Clear the screen.
        pygame.display.get_surface().fill(Colors.White.getTuple())

        # Update Game
        circleGame.update(deltaTime)

        # Draw Game
        circleGame.draw(deltaTime)

        # Update the window title.
        pygame.display.set_caption("{} - {:6.3f} FPS".format(gameTitle, fpsClock.get_fps()))

        # Update the screen.
        pygame.display.flip()
        pygame.display.update()

        # Handle input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameDone = True
            circleGame.handleInput(event)
        
    print("Exiting game...", end='')

    # Stop all audio channels.
    pygame.mixer.stop()

    # Delete cache from memory.
    AssetCache.unloadCache()

    # Uninitialize PyGame Mixer.
    pygame.mixer.quit()

    # Uninitialize PyGame TTF.
    pygame.font.quit()

    # Uninitialize PyGame.
    pygame.quit()

    print(" done!")

def drawFPSText(font, position, text, color, screen):
    textSurface = font.render(text, True, color.getTuple())
    screen.blit(textSurface, (position.x, position.y))

def exitGame():
    global gameDone
    gameDone = True
