# GameInit.py - Initializes PyGame and our game, and it contains the game loop.
# Created by Josh Kennedy on 17 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015 Sirkles LLC

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
import HelperAPI

# Our global loop condition, so we can exit the game from the menu.
gameDone = False

# Initializes PyGame and its subsystems.
def initialize():
    # Print the OS details.
    print("Detected OS: %s %s %s\n" % (platform.system(), platform.release(), platform.version()))

    # Print the Python details.
    print("Detected Python Version: " + platform.python_implementation() + ' ' + platform.python_version())
    print("Using Python installed at: " + sys.executable + '\n')

    print("Starting up...", end='')

    # Set up environment variables for SDL (PyGame's subsystem).
    os.environ["SDL_VIDEO_CENTERED"] = '1' # Centers the screen.

    if platform.system() == "Windows":
        os.environ["SDL_VIDEODRIVER"] = "directx" # If we're running Windows, then use the DirectX video driver.
    elif platform.system() == "Darwin":
        os.environ["SDL_VIDEODRIVER"] = "Quartz" # If we're running OS X (Darwin), then use Core Graphics.
    else:
        os.environ["SDL_VIDEODRIVER"] = "x11" # Otherwise, just use X11 (even though it sucks.)

    # Initialize PyGame TTF.
    pygame.font.init()

    # Initialize PyGame Mixer.
    pygame.mixer.pre_init(44100, -16, 1, 512) # I don't know what these values mean, but they work best.

    # Initialize PyGame.
    pygame.init()

    # Load and cache the assets.
    AssetCache.startCache(os.path.dirname(os.path.realpath(__file__)) + "/Resources/")

    # Initialize the window to 720p.
    screen = pygame.display.set_mode(AssetCache.screenResolution, pygame.HWACCEL | pygame.DOUBLEBUF)
    pygame.display.set_caption("Pop a Dots (Python)", "Pop a Dots")

    # Set icon.
    pygame.display.set_icon(pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + "/Resources/Icon_Full.png"))

    # Clear the screen to white, and update it.
    screen.fill(Colors.White.getTuple())
    pygame.display.flip()

    # aaaand we're done!
    print(" done!")

    # Print out graphics driver details, just so we know.
    print("\nDetected Graphics Driver: " + pygame.display.get_driver() + '\n')

# Kickstarts the game.
def start():
    global gameDone

    print("Initializing... ", end='')

    fps = 60 # Our FPS, obviously.
    fpsClock = pygame.time.Clock() # The clock that's going to keep track of the current FPS.

    # Initialize and seed the pseudo-random number generator.
    random.seed()

    # Create an instance of the Circle Game.
    circleGame = CirclesGame.CirclesGame()

    print(" done!\n")

    lastFrame = time.time()

    # Set the initial value to gameDone
    gameDone = False

    gameTitle = "Pop a Dots (Python)"

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

        # Handle input.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameDone = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F12:
                    HelperAPI.takeScreenshot()

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
