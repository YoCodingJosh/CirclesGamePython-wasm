# GameInit.py - Initializes PyGame and our game, and it contains the game loop.
# Created by Josh Kennedy on 17 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import os
import sys
import platform
import pygame

import Colors
import Vector2
import Circle

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

    # Initialize the window.
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

    done = False
    fps = 60
    fpsClock = pygame.time.Clock()

    font = pygame.font.SysFont("Arial", 20, True)

    testCircle = Circle.Circle(500, 500, 100)

    print(" done!")

    # The game loop.
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # test circle, please ignore
        testCircle.draw(Colors.Purple)

        # Update the screen.
        pygame.display.flip()
        pygame.display.update()

        # Clear the screen.
        pygame.display.get_surface().fill(Colors.White.getTuple())

        # Draw the FPS
        drawText(font, Vector2.Vector2(0, 0), "FPS: %6.3f" % fpsClock.get_fps(), Colors.Black, pygame.display.get_surface())

        # Calculate the fps.
        fpsClock.tick(fps)
        
    # Uninitialize PyGame.
    pygame.quit()

def drawText(font, position, text, color, screen):
    textSurface = font.render(text, True, color.getTuple())
    screen.blit(textSurface, (position.x, position.y))
